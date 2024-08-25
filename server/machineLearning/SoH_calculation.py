import sqlite3
import pandas as pd
import numpy as np
from scipy.integrate import simps

def calculate_data_driven_soh(db_path, cell_id, debug=False):
    """
    Calculate a data-driven State of Health (SoH) for a specific EV battery cell.
    
    :param db_path: Path to the SQLite database
    :param cell_id: ID of the cell to analyze
    :param debug: If True, print diagnostic information
    :return: float representing the estimated SoH as a percentage, or None if calculation fails
    """
    try:
        conn = sqlite3.connect(db_path)
        
        # Load data for the specific cell
        overview = pd.read_sql_query(f"SELECT * FROM Overview WHERE Cell_ID = '{cell_id}' ORDER BY CheckUp_ID", conn)
        eis = pd.read_sql_query(f"SELECT * FROM EIS WHERE file_name LIKE '{cell_id}%'", conn)
        ocv = pd.read_sql_query(f"SELECT * FROM OCV WHERE file_name LIKE '{cell_id}%'", conn)
        capacity_raw = pd.read_sql_query(f"SELECT * FROM capacity_raw WHERE file_name LIKE '{cell_id}%'", conn)
        qocv = pd.read_sql_query(f"SELECT * FROM qOCV WHERE file_name LIKE '{cell_id}%'", conn)
        
        conn.close()

        if overview.empty or eis.empty or ocv.empty or capacity_raw.empty or qocv.empty:
            print(f"No data found for cell {cell_id}")
            return None

        # 1. Capacity fade
        initial_capacity = overview['Capacity'].iloc[0]
        current_capacity = overview['Capacity'].iloc[-1]
        capacity_fade = (current_capacity / initial_capacity) * 100

        # 2. Impedance growth
        initial_impedance = eis[eis['file_name'] == eis['file_name'].unique()[0]]['Impedance'].mean()
        current_impedance = eis[eis['file_name'] == eis['file_name'].unique()[-1]]['Impedance'].mean()
        impedance_growth = (initial_impedance / current_impedance) * 100

        # 3. Pulse resistance increase
        initial_pulse_resistance = overview['ten_seconds_Pulse_Resistance'].iloc[0]
        current_pulse_resistance = overview['ten_seconds_Pulse_Resistance'].iloc[-1]
        pulse_resistance_increase = (initial_pulse_resistance / current_pulse_resistance) * 100

        # 4. OCV curve shift
        initial_ocv = ocv[ocv['file_name'] == ocv['file_name'].unique()[0]]
        current_ocv = ocv[ocv['file_name'] == ocv['file_name'].unique()[-1]]
        ocv_shift = 1 - np.nanmean(abs(initial_ocv['Open_Circuit_Voltage'] - current_ocv['Open_Circuit_Voltage']))
        ocv_shift = 1 if np.isnan(ocv_shift) else np.clip(ocv_shift, 0, 1)

        # 5. Charge throughput
        charge_data = capacity_raw[capacity_raw['Current'] > 0]
        discharge_data = capacity_raw[capacity_raw['Current'] < 0]
        total_charge = max(0, simps(charge_data['Current'], charge_data['Time']) / 3600)  # Ensure non-negative
        total_discharge = max(0, abs(simps(discharge_data['Current'], discharge_data['Time'])) / 3600)  # Ensure non-negative
        total_throughput = min(max(total_charge, total_discharge), initial_capacity * 10000)  # Cap at 10000 full cycles
        equivalent_cycles = total_throughput / initial_capacity
        charge_throughput_factor = np.exp(-equivalent_cycles / 1750)  # Using 1750 as midpoint of 1500-2000 range

        # 6. Cycling age
        cycle_count = min(overview['Cycles_or_Days_of_Aging_Test'].max(), 10000)  # Cap at 10000 cycles
        cycling_age_factor = np.exp(-cycle_count / 1750)  # Using 1750 as midpoint of 1500-2000 range

        # 7. Temperature stress
        avg_temp = capacity_raw['Cell_Temperature'].mean()
        temp_stress_factor = 1 - min(abs(avg_temp - 25) / 50, 1)  # Ensure factor is between 0 and 1

        # 8. SOC usage
        soc_range = min(qocv['SOC'].max() - qocv['SOC'].min(), 100)  # Ensure range is not greater than 100
        soc_usage_factor = 0.5 + 0.5 * (1 - soc_range / 100)  # Adjusted to never be zero

        # Combine all factors
        weights = {
            'capacity_fade': 0.50,
            'impedance_growth': 0.15,
            'pulse_resistance_increase': 0.15,
            'ocv_shift': 0.05,
            'charge_throughput': 0.05,
            'cycling_age': 0.05,
            'temp_stress': 0.03,
            'soc_usage': 0.02
        }

        soh = (
            weights['capacity_fade'] * capacity_fade +
            weights['impedance_growth'] * impedance_growth +
            weights['pulse_resistance_increase'] * pulse_resistance_increase +
            weights['ocv_shift'] * ocv_shift * 100 +
            weights['charge_throughput'] * charge_throughput_factor * 100 +
            weights['cycling_age'] * cycling_age_factor * 100 +
            weights['temp_stress'] * temp_stress_factor * 100 +
            weights['soc_usage'] * soc_usage_factor * 100
        )

        if debug:
            print(f"Capacity fade: {capacity_fade:.2f}%")
            print(f"Impedance growth: {impedance_growth:.2f}%")
            print(f"Pulse resistance increase: {pulse_resistance_increase:.2f}%")
            print(f"OCV shift: {ocv_shift:.4f}")
            print(f"Total charge: {total_charge:.2f} Ah")
            print(f"Total discharge: {total_discharge:.2f} Ah")
            print(f"Equivalent cycles: {equivalent_cycles:.2f}")
            print(f"Charge throughput factor: {charge_throughput_factor:.4f}")
            print(f"Cycle count: {cycle_count}")
            print(f"Cycling age factor: {cycling_age_factor:.4f}")
            print(f"Average temperature: {avg_temp:.2f}°C")
            print(f"Temperature stress factor: {temp_stress_factor:.4f}")
            print(f"SOC range: {soc_range:.2f}%")
            print(f"SOC usage factor: {soc_usage_factor:.4f}")

        return max(0, min(soh, 100))  # Ensure SoH is between 0 and 100

    except Exception as e:
        print(f"Error calculating SoH for cell {cell_id}: {str(e)}")
        return None

# Example usage:
soh = calculate_data_driven_soh('path_to_database.db', 'cell_ID', debug=True)
if soh is not None:
    print(f"The estimated State of Health for cell_ID is: {soh:.2f}%")
else:
     print("Failed to calculate SoH")
