import sqlite3

# make a database file that has 5 tables
# table 1: users (userID (PK), email, password, firstName, lastName, phone, profilePicLink, completeGoogleJWT, isAdmin)
# table 2: owns (userID, carID)
# table 3: cars (carID (PK), carModel, carName, batteryCap, nominalVolt)
# table 4: Journey (journeyID (PK), userID (FK), carID (FK), startLocation, endLocation, startTime, endTime, distance, startRecordID, endRecordID)
# table 5: records (recordID (PK), carID, time, location, stateOfCharge, range, power, temperature)

# with the following relationships:
"""
users (userID) -> owns (userID) -- one and only to many
cars (carID) -> owns (carID) -- one and only to many
users (userID) -> journey (userID) -- one and only to many
cars (carID) -> journey (carID) -- one and only to many
cars (carID) -> records (carID) -- one and only to many
journey (startRecordID) -> records (recordID) -- one and only to one
journey (endRecordID) -> records (recordID) -- one and only to one
"""

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
 
    # Create tables

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                userID SERIAL PRIMARY KEY,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                firstName TEXT NOT NULL,
                lastName TEXT NOT NULL,
                phone TEXT NOT NULL,
                profilePicLink TEXT,
                completeGoogleJWT TEXT,
                isAdmin BOOLEAN NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cars (
                carID SERIAL PRIMARY KEY,
                userID SERIAL,
                carModel TEXT NOT NULL,
                carName TEXT NOT NULL,
                batteryCap REAL NOT NULL,
                nominalVolt REAL NOT NULL,
                FOREIGN KEY (userID) REFERENCES users(userID)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS journey (
                journeyID SERIAL PRIMARY KEY,
                userID SERIAL,
                carID SERIAL,
                startLocation TEXT NOT NULL,
                endLocation TEXT NOT NULL,
                startTime TEXT NOT NULL,
                endTime TEXT NOT NULL,
                distance REAL NOT NULL,
                startRecordID INTEGER NOT NULL,
                endRecordID INTEGER NOT NULL,
                FOREIGN KEY (userID) REFERENCES users(userID),
                FOREIGN KEY (carID) REFERENCES cars(carID),
                FOREIGN KEY (startRecordID) REFERENCES records(recordID),
                FOREIGN KEY (endRecordID) REFERENCES records(recordID)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                recordID SERIAL PRIMARY KEY,
                carID SERIAL,
                time DATETIME NOT NULL,
                location TEXT NOT NULL,
                stateOfCharge REAL NOT NULL,
                range REAL NOT NULL,
                power REAL NOT NULL,
                temperature REAL NOT NULL,
                FOREIGN KEY (carID) REFERENCES cars(carID)
            )
        ''')

        self.conn.commit()

    # Drop tables

    def drop_tables(self):
        self.cursor.execute('''
            DROP TABLE IF EXISTS users
        ''')

        self.cursor.execute(''' 
            DROP TABLE IF EXISTS cars
        ''')

        self.cursor.execute(''' 
            DROP TABLE IF EXISTS journey
        ''')

        self.cursor.execute('''
            DROP TABLE IF EXISTS records
        ''')

        self.conn.commit()

    def close(self):
        self.conn.close()

    # Insert functions

    def insert_user(self, email, password, firstName, lastName, phone, profilePicLink, completeGoogleJWT, isAdmin):
        self.cursor.execute('''
            INSERT INTO users (email, password, firstName, lastName, phone, profilePicLink, completeGoogleJWT, isAdmin)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (email, password, firstName, lastName, phone, profilePicLink, completeGoogleJWT, isAdmin))
        self.conn.commit()

    def insert_car(self, carModel, carName, batteryCap, nominalVolt):
        self.cursor.execute('''
            INSERT INTO cars (carModel, carName, batteryCap, nominalVolt)
            VALUES (?, ?, ?, ?)
        ''', (carModel, carName, batteryCap, nominalVolt))
        self.conn.commit()

    def insert_journey(self, userID, carID, startLocation, endLocation, startTime, endTime, distance, startRecordID, endRecordID):
        self.cursor.execute('''
            INSERT INTO journey (userID, carID, startLocation, endLocation, startTime, endTime, distance, startRecordID, endRecordID)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (userID, carID, startLocation, endLocation, startTime, endTime, distance, startRecordID, endRecordID))
        self.conn.commit()

    def insert_record(self, carID, time, location, stateOfCharge, range, power, temperature):
        self.cursor.execute('''
            INSERT INTO records (carID, time, location, stateOfCharge, range, power, temperature)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (carID, time, location, stateOfCharge, range, power, temperature))
        self.conn.commit()

    # Get functions

    def get_user(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def get_user_by_id(self, user_id):
        self.cursor.execute('SELECT * FROM users WHERE userID = ?', (user_id,))
        return self.cursor.fetchone()

    def get_user_by_first_name(self, first_name):
        self.cursor.execute('SELECT * FROM users WHERE firstName = ?', (first_name,))
        return self.cursor.fetchall()

    def get_user_by_last_name(self, last_name):
        self.cursor.execute('SELECT * FROM users WHERE lastName = ?', (last_name,))
        return self.cursor.fetchall()

    def get_user_by_email(self, email):
        self.cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        return self.cursor.fetchall()

    def get_user_by_phone(self, phone):
        self.cursor.execute('SELECT * FROM users WHERE phone = ?', (phone,))
        return self.cursor.fetchall()

    def get_user_by_is_admin(self, is_admin):
        self.cursor.execute('SELECT * FROM users WHERE isAdmin = ?', (is_admin,))
        return self.cursor.fetchall()
    
    def get_user_password(self, email, user_id):
        self.cursor.execute('SELECT password FROM users WHERE email = ? AND userID = ?', (email, user_id))
        return self.cursor.fetchall()

    def get_car(self):
        self.cursor.execute('SELECT * FROM cars')
        return self.cursor.fetchall()

    def get_car_by_user(self):
        self.cursor.execute('SELECT * FROM cars JOIN users ON cars.userID = users.userID')
        return self.cursor.fetchall()

    def get_car_by_car_name(self, car_name):
        self.cursor.execute('SELECT * FROM cars WHERE carName = ?', (car_name,))
        return self.cursor.fetchall()

    def get_journey(self):
        self.cursor.execute('SELECT * FROM journey')
        return self.cursor.fetchall()

    def get_journey_by_user(self):
        self.cursor.execute('SELECT * FROM journey JOIN users ON journey.userID = users.userID')
        return self.cursor.fetchall()

    def get_journey_by_car(self):
        self.cursor.execute('SELECT * FROM journey JOIN cars ON journey.carID = cars.carID')
        return self.cursor.fetchall()

    def get_journey_by_record(self):
        self.cursor.execute('SELECT * FROM journey JOIN records ON journey.startRecordID = records.recordID OR journey.endRecordID = records.recordID')
        return self.cursor.fetchall()

    def get_records(self):
        self.cursor.execute('SELECT * FROM records')
        return self.cursor.fetchall()

    def get_record_by_car(self):
        self.cursor.execute('SELECT * FROM records JOIN cars ON records.carID = cars.carID')
        return self.cursor.fetchall()
    
    def get_record_by_journey(self):
        self.cursor.execute('SELECT * FROM records JOIN journey ON records.recordID = journey.startRecordID OR records.recordID = journey.endRecordID')
        return self.cursor.fetchall()
    
    # Update functions

    def update_user_password(self, email, user_id, new_password):
        self.cursor.execute('UPDATE users SET password = ? WHERE email = ? AND userID = ?', (new_password, email, user_id))
        self.conn.commit()

    def update_user_first_name(self, user_id, new_first_name):
        self.cursor.execute('UPDATE users SET firstName = ? WHERE userID = ?', (new_first_name, user_id))
        self.conn.commit()

    def update_user_last_name(self, user_id, new_last_name):
        self.cursor.execute('UPDATE users SET lastName = ? WHERE userID = ?', (new_last_name, user_id))
        self.conn.commit()

    def update_user_email(self, user_id, email, new_email):
        self.cursor.execute('UPDATE users SET email = ? WHERE userID = ? AND email = ?', (new_email, user_id, email))
        self.conn.commit()

    def update_user_profile_picture(self, user_id, new_profile_pic_link):
        self.cursor.execute('UPDATE users SET profilePicLink = ? WHERE userID = ?', (new_profile_pic_link, user_id))
        self.conn.commit()

    def update_user_phone(self, user_id, new_phone):
        self.cursor.execute('UPDATE users SET phone = ? WHERE userID = ?', (new_phone, user_id))
        self.conn.commit()

    def update_user_is_admin(self, user_id, new_is_admin):
        self.cursor.execute('UPDATE users SET isAdmin = ? WHERE userID = ?', (new_is_admin, user_id))
        self.conn.commit()

    def update_car_model(self, car_id, user_id, new_car_model):
        self.cursor.execute('UPDATE cars SET carModel = ? WHERE carID = ? AND userID = ?', (new_car_model, car_id, user_id))
        self.conn.commit()

    def update_car_name(self, car_id, user_id, new_car_name):
        self.cursor.execute('UPDATE cars SET carName = ? WHERE carID = ? AND userID = ?', (new_car_name, car_id, user_id))
        self.conn.commit()

    def update_car_battery_cap(self, car_id, user_id, new_battery_cap):
        self.cursor.execute('UPDATE cars SET batteryCap = ? WHERE carID = ? AND userID = ?', (new_battery_cap, car_id, user_id))
        self.conn.commit()

    def update_car_nominal_volt(self, car_id, user_id, new_nominal_volt):
        self.cursor.execute('UPDATE cars SET nominalVolt = ? WHERE carID = ? AND userID = ?', (new_nominal_volt, car_id, user_id))
        self.conn.commit()

if __name__ == '__main__':
    db = Database('database.db')
    db.create_tables()



