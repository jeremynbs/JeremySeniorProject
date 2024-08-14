# EV Car Battery Cell Checkups Dataset
## Overview
This table contains several categories of data related  to the health of the battery cells of the EV.

Data is obtained from SiCWell Dataset in IEEE DataPort. The dataset is available at https://ieee-dataport.org/open-access/sicwell-dataset
## Cell Checkups
The periodic checkups of the battery cells are composed of capacity, internal resistance, EIS, OCV, and qOCV measurements. Measurements that take longer, such as EIS and OCV, are not taken at every checkup. The results are stored in the “cell_checkups” database with the following tables:

## Categories
Each category is stored in a separate table. The tables are as follows:

1. Capacity_raw: Raw current, voltage, and temperature values of the capacity measurement.
2. EIS: The results of the electrochemical impedance spectroscopy from 0.001 to 50,000 Hz using an EIS-meter.
3. OCV: Results of the open-circuit voltage measurement between 0 and 100 % State of Charge in 5 % steps.
4. qOCV: Results of the quasi-open-circuit voltage measurement between 0 and 100 % State of Charge in 1 % steps. It contains the quasi-open-circuit voltage, 1s resistance, and 10s resistance.

## Attributes
### Capacity_raw
1. Time - (Seconds)
2. Current - (Ampere)
3. Cell_Voltage - (Volt)
4. Cell_Temperature - (Celsius)
5. Temperature_at_Cell_Connector - (Celsius)
6. file_name

### EIS
1. SOC - (Percentage)
2. Frequency - (Hz)
3. Impedance - (Ohm)
4. file_name

### OCV
1. Current_Direction
2. SOC - (Percentage)
3. Removed_Charge - (Ah)
4. Open_Circuit_Voltage - (Volt)
5. file_name

### qOCV
1. Current_Direction
2. SOC - (Percentage)
3. Removed_Charge - (Ah)
4. Quasi_Open_Circuit_Voltage - (Volt)
5. one_second_Pulse_Resistance - (Ohm)
6. ten_seconds_Pulse_Resistance - (Ohm)
7. file_name

## Relations
The relations between each table are available in Overview.csv file or Overview.db
The columns in the Overview.csv file are as follows:
1. Cell_ID
2. CheckUp_ID
3. CheckUp_Date - (YYYY-MM-DD)
4. Cycles_or_Days_of_Aging - (Cycles for Cell ID beginning with AC and DC, Days of Aging for Cell ID beginning with KA)
5. ten_seconds_Pulse_Resistance - (Ohm)
6. Capacity - (Ah)
7. Filename_Raw_Data_Capacity_Measurement - (Capacity_raw Table, file_name column)
8. Filename_Impedance_Measurement - (EIS Table, file_name column)
9. Filename_OCV_Data - (OCV Table, file_name column)
10. Filename_qOCV_Data - (qOCV Table, file_name column)

## Cell Aging Scenarios
The battery cells are cycled in groups of three cells in series. The scenarios for each cell are the following:

* Ka01, Ka02: Calendar test 35°C 80% SoC
* Ka03, Ka04: Calendar test 35°C 45% SoC
* Ka05, Ka06: Calendar test 45°C 80% SoC 
* Ka07, Ka08: Calendar test 45°C 20% SoC
* Ka09, Ka10: Calendar test 45°C 45% SoC
* Ka11, Ka12: Calendar test 45°C 60% SoC
* DC01, DC02, DC03: DC cycling
* AC01, AC02, AC03: Sinusoidal cycling 10 kHz, 12.5 A
* AC04, AC05, AC06: Sinusoidal cycling 10 kHz, 25.0 A
* AC07, AC08, AC09: Sinusoidal cycling 10 kHz, 6.25 A
* AC10, AC11, AC12: Sinusoidal cycling 40 kHz, 12.5 A
* AC13, AC14, AC15: Sinusoidal cycling 20 kHz, 12.5 A
* AC16, AC17, AC18: Sinusoidal cycling 40 kHz, 6.25 A
* AC19, AC20, AC21: Artificial ripple cycling
* AC22, AC23, AC24: Realistic ripple cycling
* AC25, AC26, AC27: Realistic ripple cycling

