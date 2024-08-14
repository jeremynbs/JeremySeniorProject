from flask import Flask, jsonify, request

import schema.tables

import schema.tables

app = Flask(__name__)

# Create an instance of the tables class
tables = schema.tables.Database()

# API route for dropping tables
@app.route('/drop_tables', methods=['POST'])
def drop_tables():
    tables.drop_tables()
    return jsonify({'message': 'Tables dropped successfully'})

# API route for closing the connection
@app.route('/close', methods=['POST'])
def close():
    tables.close()
    return jsonify({'message': 'Connection closed successfully'})

##################################
# API routes for inserting data
##################################

# API route for inserting a user
@app.route('/insert_user', methods=['POST'])
def insert_user():
    # Get the request data
    data = request.get_json()
    email = data['email']
    password = data['password']
    firstName = data['firstName']
    lastName = data['lastName']
    phone = data['phone']
    profilePicLink = data['profilePicLink']
    completeGoogleJWT = data['completeGoogleJWT']
    isAdmin = data['isAdmin']
    
    # Insert the user into the database
    tables.insert_user(email, password, firstName, lastName, phone, profilePicLink, completeGoogleJWT, isAdmin)
    
    return jsonify({'message': 'User inserted successfully'})

# API route for inserting a car
@app.route('/insert_car', methods=['POST'])
def insert_car():
    # Get the request data
    data = request.get_json()
    carModel = data['carModel']
    carName = data['carName']
    batteryCap = data['batteryCap']
    nominalVolt = data['nominalVolt']
    
    # Insert the car into the database
    tables.insert_car(carModel, carName, batteryCap, nominalVolt)
    
    return jsonify({'message': 'Car inserted successfully'})

# API route for inserting a journey
@app.route('/insert_journey', methods=['POST'])
def insert_journey():
    # Get the request data
    data = request.get_json()
    userID = data['userID']
    carID = data['carID']
    startLocation = data['startLocation']
    endLocation = data['endLocation']
    startTime = data['startTime']
    endTime = data['endTime']
    distance = data['distance']
    startRecordID = data['startRecordID']
    endRecordID = data['endRecordID']
    
    # Insert the journey into the database
    tables.insert_journey(userID, carID, startLocation, endLocation, startTime, endTime, distance, startRecordID, endRecordID)
    
    return jsonify({'message': 'Journey inserted successfully'})

# API route for inserting a record
@app.route('/insert_record', methods=['POST'])
def insert_record():
    # Get the request data
    data = request.get_json()
    carID = data['carID']
    time = data['time']
    location = data['location']
    stateOfCharge = data['stateOfCharge']
    range = data['range']
    power = data['power']
    temperature = data['temperature']
    
    # Insert the record into the database
    tables.insert_record(carID, time, location, stateOfCharge, range, power, temperature)
    
    return jsonify({'message': 'Record inserted successfully'})

##################################
# API routes for user table operations
##################################

# GET routes
# API route for getting all users
@app.route('/get_users', methods=['GET'])
def get_users():
    users = tables.get_user()
    return jsonify(users)

# API route for getting a user by ID
@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = tables.get_user_by_id(user_id)
    return jsonify(user)

# API route for getting users by first name
@app.route('/get_users_by_first_name/<string:first_name>', methods=['GET'])
def get_users_by_first_name(first_name):
    users = tables.get_user_by_first_name(first_name)
    return jsonify(users)

# API route for getting users by last name
@app.route('/get_users_by_last_name/<string:last_name>', methods=['GET'])
def get_users_by_last_name(last_name):
    users = tables.get_user_by_last_name(last_name)
    return jsonify(users)

# API route for getting users by email
@app.route('/get_users_by_email/<string:email>', methods=['GET'])
def get_users_by_email(email):
    users = tables.get_user_by_email(email)
    return jsonify(users)

# API route for getting users by phone
@app.route('/get_users_by_phone/<string:phone>', methods=['GET'])
def get_users_by_phone(phone):
    users = tables.get_user_by_phone(phone)
    return jsonify(users)

# API route for getting users by isAdmin
@app.route('/get_users_by_is_admin/<int:is_admin>', methods=['GET'])
def get_users_by_is_admin(is_admin):
    users = tables.get_user_by_is_admin(is_admin)
    return jsonify(users)

# PUT routes
# API route for updating a user's password
@app.route('/update_user_password', methods=['PUT'])
def update_user_password():
    # Get the request data
    data = request.get_json()
    email = data['email']
    user_id = data['user_id']
    new_password = data['new_password']
    
    # Update the user's password in the database
    tables.update_user_password(email, user_id, new_password)
    
    return jsonify({'message': 'User password updated successfully'})

# API route for updating a user's first name
@app.route('/update_user_first_name', methods=['PUT'])
def update_user_first_name():
    # Get the request data
    data = request.get_json()
    user_id = data['user_id']
    new_first_name = data['new_first_name']
    
    # Update the user's first name in the database
    tables.update_user_first_name(user_id, new_first_name)
    
    return jsonify({'message': 'User first name updated successfully'})

# API route for updating a user's last name
@app.route('/update_user_last_name', methods=['PUT'])
def update_user_last_name():
    # Get the request data
    data = request.get_json()
    user_id = data['user_id']
    new_last_name = data['new_last_name']
    
    # Update the user's last name in the database
    tables.update_user_last_name(user_id, new_last_name)
    
    return jsonify({'message': 'User last name updated successfully'})

# API route for updating a user's email
@app.route('/update_user_email', methods=['PUT'])
def update_user_email():
    # Get the request data
    data = request.get_json()
    user_id = data['user_id']
    email = data['email']
    new_email = data['new_email']
    
    # Update the user's email in the database
    tables.update_user_email(user_id, email, new_email)
    
    return jsonify({'message': 'User email updated successfully'})

# API route for updating a user's profile picture
@app.route('/update_user_profile_picture', methods=['PUT'])
def update_user_profile_picture():
    # Get the request data
    data = request.get_json()
    user_id = data['user_id']
    new_profile_pic_link = data['new_profile_pic_link']
    
    # Update the user's profile picture in the database
    tables.update_user_profile_picture(user_id, new_profile_pic_link)
    
    return jsonify({'message': 'User profile picture updated successfully'})

# API route for updating a user's phone
@app.route('/update_user_phone', methods=['PUT'])
def update_user_phone():
    # Get the request data
    data = request.get_json()
    user_id = data['user_id']
    new_phone = data['new_phone']
    
    # Update the user's phone in the database
    tables.update_user_phone(user_id, new_phone)
    
    return jsonify({'message': 'User phone updated successfully'})

# API route for updating a user's isAdmin
@app.route('/update_user_is_admin', methods=['PUT'])
def update_user_is_admin():
    # Get the request data
    data = request.get_json()
    user_id = data['user_id']
    new_is_admin = data['new_is_admin']
    
    # Update the user's isAdmin in the database
    tables.update_user_is_admin(user_id, new_is_admin)
    
    return jsonify({'message': 'User isAdmin updated successfully'})

##################################
# API routes for car table operations
##################################

# GET routes
# API route for getting all cars
@app.route('/get_cars', methods=['GET'])
def get_cars():
    cars = tables.get_car()
    return jsonify(cars)

# API route for getting cars by user
@app.route('/get_cars_by_user', methods=['GET'])
def get_cars_by_user():
    cars = tables.get_car_by_user()
    return jsonify(cars)

# API route for getting cars by car name
@app.route('/get_cars_by_car_name/<string:car_name>', methods=['GET'])
def get_cars_by_car_name(car_name):
    cars = tables.get_car_by_car_name(car_name)
    return jsonify(cars)

# API route for updating a car's model
@app.route('/update_car_model', methods=['PUT'])
def update_car_model():
    # Get the request data
    data = request.get_json()
    car_id = data['car_id']
    user_id = data['user_id']
    new_car_model = data['new_car_model']
    
    # Update the car's model in the database
    tables.update_car_model(car_id, user_id, new_car_model)
    
    return jsonify({'message': 'Car model updated successfully'})

# PUT routes
# API route for updating a car's name
@app.route('/update_car_name', methods=['PUT'])
def update_car_name():
    # Get the request data
    data = request.get_json()
    car_id = data['car_id']
    user_id = data['user_id']
    new_car_name = data['new_car_name']
    
    # Update the car's name in the database
    tables.update_car_name(car_id, user_id, new_car_name)
    
    return jsonify({'message': 'Car name updated successfully'})

# API route for updating a car's battery capacity
@app.route('/update_car_battery_cap', methods=['PUT'])
def update_car_battery_cap():
    # Get the request data
    data = request.get_json()
    car_id = data['car_id']
    user_id = data['user_id']
    new_battery_cap = data['new_battery_cap']
    
    # Update the car's battery capacity in the database
    tables.update_car_battery_cap(car_id, user_id, new_battery_cap)
    
    return jsonify({'message': 'Car battery capacity updated successfully'})

# API route for updating a car's nominal voltage
@app.route('/update_car_nominal_volt', methods=['PUT'])
def update_car_nominal_volt():
    # Get the request data
    data = request.get_json()
    car_id = data['car_id']
    user_id = data['user_id']
    new_nominal_volt = data['new_nominal_volt']
    
    # Update the car's nominal voltage in the database
    tables.update_car_nominal_volt(car_id, user_id, new_nominal_volt)
    
    return jsonify({'message': 'Car nominal voltage updated successfully'})

##################################
# API routes for journey table operations
##################################

# GET routes
# API route for getting all journeys
@app.route('/get_journeys', methods=['GET'])
def get_journeys():
    journeys = tables.get_journey()
    return jsonify(journeys)

# API route for getting journeys by user
@app.route('/get_journeys_by_user', methods=['GET'])
def get_journeys_by_user():
    journeys = tables.get_journey_by_user()
    return jsonify(journeys)

# API route for getting journeys by car
@app.route('/get_journeys_by_car', methods=['GET'])
def get_journeys_by_car():
    journeys = tables.get_journey_by_car()
    return jsonify(journeys)

# API route for getting journeys by record
@app.route('/get_journeys_by_record', methods=['GET'])
def get_journeys_by_record():
    journeys = tables.get_journey_by_record()
    return jsonify(journeys)

##################################
#  API routes for record table operations
##################################

# GET routes
# API route for getting all records
@app.route('/get_records', methods=['GET'])
def get_records():
    records = tables.get_records()
    return jsonify(records)

# API route for getting records by car
@app.route('/get_records_by_car', methods=['GET'])
def get_records_by_car():
    records = tables.get_record_by_car()
    return jsonify(records)

# API route for getting records by journey
@app.route('/get_records_by_journey', methods=['GET'])
def get_records_by_journey():
    records = tables.get_record_by_journey()
    return jsonify(records)


if __name__ == '__main__':
    app.run(debug=True)