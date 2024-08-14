# API Documentation

## Table of Contents
- [Insert User](#insert-user)
- [Insert Car](#insert-car)
- [Insert Journey](#insert-journey)
- [Insert Record](#insert-record)
- [Get Users](#get-users)
- [Get User by ID](#get-user-by-id)
- [Get Users by First Name](#get-users-by-first-name)
- [Get Users by Last Name](#get-users-by-last-name)
- [Get Users by Email](#get-users-by-email)
- [Get Users by Phone](#get-users-by-phone)
- [Get Users by isAdmin](#get-users-by-is-admin)
- [Update User Password](#update-user-password)
- [Update User First Name](#update-user-first-name)
- [Update User Last Name](#update-user-last-name)
- [Update User Email](#update-user-email)
- [Update User Profile Picture](#update-user-profile-picture)
- [Update User Phone](#update-user-phone)
- [Update User isAdmin](#update-user-is-admin)
- [Get Cars](#get-cars)
- [Get Cars by User](#get-cars-by-user)
- [Get Cars by Car Name](#get-cars-by-car-name)
- [Update Car Model](#update-car-model)
- [Update Car Name](#update-car-name)
- [Update Car Battery Capacity](#update-car-battery-cap)
- [Update Car Nominal Voltage](#update-car-nominal-volt)
- [Get Journeys](#get-journeys)
- [Get Journeys by User](#get-journeys-by-user)
- [Get Journeys by Car](#get-journeys-by-car)
- [Get Journeys by Record](#get-journeys-by-record)
- [Get Records](#get-records)
- [Get Records by Car](#get-records-by-car)
- [Get Records by Journey](#get-records-by-journey)

## Insert User
- **Endpoint:** `/insert_user`
- **Method:** POST
- **Description:** Inserts a new user into the database.
- **Request Body:**
    ```json
    {
        "email": "user@example.com",
        "password": "password123",
        "firstName": "John",
        "lastName": "Doe",
        "phone": "1234567890",
        "profilePicLink": "https://example.com/profile.jpg",
        "completeGoogleJWT": "google-jwt-token",
        "isAdmin": 0
    }
    ```
- **Response:** `{'message': 'User inserted successfully'}`

## Insert Car
- **Endpoint:** `/insert_car`
- **Method:** POST
- **Description:** Inserts a new car into the database.
- **Request Body:**
    ```json
    {
        "carModel": "Tesla Model S",
        "carName": "My Car",
        "batteryCap": 75,
        "nominalVolt": 400
    }
    ```
- **Response:** `{'message': 'Car inserted successfully'}`

## Insert Journey
- **Endpoint:** `/insert_journey`
- **Method:** POST
- **Description:** Inserts a new journey into the database.
- **Request Body:**
    ```json
    {
        "userID": 1,
        "carID": 1,
        "startLocation": "New York",
        "endLocation": "Los Angeles",
        "startTime": "2022-01-01 12:00:00",
        "endTime": "2022-01-01 18:00:00",
        "distance": 300,
        "startRecordID": 1,
        "endRecordID": 10
    }
    ```
- **Response:** `{'message': 'Journey inserted successfully'}`

## Insert Record
- **Endpoint:** `/insert_record`
- **Method:** POST
- **Description:** Inserts a new record into the database.
- **Request Body:**
    ```json
    {
        "carID": 1,
        "time": "2022-01-01 12:00:00",
        "location": "New York",
        "stateOfCharge": 80,
        "range": 200,
        "power": 100,
        "temperature": 25
    }
    ```
- **Response:** `{'message': 'Record inserted successfully'}`

## Get Users
- **Endpoint:** `/get_users`
- **Method:** GET
- **Description:** Retrieves all users from the database.
- **Response:** Array of user objects.

## Get User by ID
- **Endpoint:** `/get_user/{user_id}`
- **Method:** GET
- **Description:** Retrieves a user by their ID from the database.
- **Response:** User object.

## Get Users by First Name
- **Endpoint:** `/get_users_by_first_name/{first_name}`
- **Method:** GET
- **Description:** Retrieves users by their first name from the database.
- **Response:** Array of user objects.

## Get Users by Last Name
- **Endpoint:** `/get_users_by_last_name/{last_name}`
- **Method:** GET
- **Description:** Retrieves users by their last name from the database.
- **Response:** Array of user objects.

## Get Users by Email
- **Endpoint:** `/get_users_by_email/{email}`
- **Method:** GET
- **Description:** Retrieves users by their email from the database.
- **Response:** Array of user objects.

## Get Users by Phone
- **Endpoint:** `/get_users_by_phone/{phone}`
- **Method:** GET
- **Description:** Retrieves users by their phone number from the database.
- **Response:** Array of user objects.

## Get Users by isAdmin
- **Endpoint:** `/get_users_by_is_admin/{is_admin}`
- **Method:** GET
- **Description:** Retrieves users by their isAdmin status from the database.
- **Response:** Array of user objects.

## Update User Password
- **Endpoint:** `/update_user_password`
- **Method:** PUT
- **Description:** Updates a user's password in the database.
- **Request Body:**
    ```json
    {
        "email": "user@example.com",
        "user_id": 1,
        "new_password": "newpassword123"
    }
    ```
- **Response:** `{'message': 'User password updated successfully'}`

## Update User First Name
- **Endpoint:** `/update_user_first_name`
- **Method:** PUT
- **Description:** Updates a user's first name in the database.
- **Request Body:**
    ```json
    {
        "user_id": 1,
        "new_first_name": "Jane"
    }
    ```
- **Response:** `{'message': 'User first name updated successfully'}`

## Update User Last Name
- **Endpoint:** `/update_user_last_name`
- **Method:** PUT
- **Description:** Updates a user's last name in the database.
- **Request Body:**
    ```json
    {
        "user_id": 1,
        "new_last_name": "Doe"
    }
    ```
- **Response:** `{'message': 'User last name updated successfully'}`

## Update User Email
- **Endpoint:** `/update_user_email`
- **Method:** PUT
- **Description:** Updates a user's email in the database.
- **Request Body:**
    ```json
    {
        "user_id": 1,
        "email": "user@example.com",
        "new_email": "newuser@example.com"
    }
    ```
- **Response:** `{'message': 'User email updated successfully'}`

## Update User Profile Picture
- **Endpoint:** `/update_user_profile_picture`
- **Method:** PUT
- **Description:** Updates a user's profile picture in the database.
- **Request Body:**
    ```json
    {
        "user_id": 1,
        "new_profile_pic_link": "https://example.com/new-profile.jpg"
    }
    ```
- **Response:** `{'message': 'User profile picture updated successfully'}`

## Update User Phone
- **Endpoint:** `/update_user_phone`
- **Method:** PUT
- **Description:** Updates a user's phone number in the database.
- **Request Body:**
    ```json
    {
        "user_id": 1,
        "new_phone": "9876543210"
    }
    ```
- **Response:** `{'message': 'User phone updated successfully'}`

## Update User isAdmin
- **Endpoint:** `/update_user_is_admin`
- **Method:** PUT
- **Description:** Updates a user's isAdmin status in the database.
- **Request Body:**
    ```json
    {
        "user_id": 1,
        "new_is_admin": 1
    }
    ```
- **Response:** `{'message': 'User isAdmin updated successfully'}`

## Get Cars
- **Endpoint:** `/get_cars`
- **Method:** GET
- **Description:** Retrieves all cars from the database.
- **Response:** Array of car objects.

## Get Cars by User
- **Endpoint:** `/get_cars_by_user`
- **Method:** GET
- **Description:** Retrieves cars by user from the database.
- **Response:** Array of car objects.

## Get Cars by Car Name
- **Endpoint:** `/get_cars_by_car_name/{car_name}`
- **Method:** GET
- **Description:** Retrieves cars by car name from the database.
- **Response:** Array of car objects.

## Update Car Model
- **Endpoint:** `/update_car_model`
- **Method:** PUT
- **Description:** Updates a car's model in the database.
- **Request Body:**
    ```json
    {
        "car_id": 1,
        "user_id": 1,
        "new_car_model": "Tesla Model 3"
    }
    ```
- **Response:** `{'message': 'Car model updated successfully'}`

## Update Car Name
- **Endpoint:** `/update_car_name`
- **Method:** PUT
- **Description:** Updates a car's name in the database.
- **Request Body:**
    ```json
    {
        "car_id": 1,
        "user_id": 1,
        "new_car_name": "My New Car"
    }
    ```
- **Response:** `{'message': 'Car name updated successfully'}`

## Update Car Battery Capacity
- **Endpoint:** `/update_car_battery_cap`
- **Method:** PUT
- **Description:** Updates a car's battery capacity in the database.
- **Request Body:**
    ```json
    {
        "car_id": 1,
        "user_id": 1,
        "new_battery_cap": 100
    }
    ```
- **Response:** `{'message': 'Car battery capacity updated successfully'}`

## Update Car Nominal Voltage
- **Endpoint:** `/update_car_nominal_volt`
- **Method:** PUT
- **Description:** Updates a car's nominal voltage in the database.
- **Request Body:**
    ```json
    {
        "car_id": 1,
        "user_id": 1,
        "new_nominal_volt": 500
    }
    ```
- **Response:** `{'message': 'Car nominal voltage updated successfully'}`

## Get Journeys
- **Endpoint:** `/get_journeys`
- **Method:** GET
- **Description:** Retrieves all journeys from the database.
- **Response:** Array of journey objects.

## Get Journeys by User
- **Endpoint:** `/get_journeys_by_user`
- **Method:** GET
- **Description:** Retrieves journeys by user from the database.
- **Response:** Array of journey objects.

## Get Journeys by Car
- **Endpoint:** `/get_journeys_by_car`
- **Method:** GET
- **Description:** Retrieves journeys by car from the database.
- **Response:** Array of journey objects.

## Get Journeys by Record
- **Endpoint:** `/get_journeys_by_record`
- **Method:** GET
- **Description:** Retrieves journeys by record from the database.
- **Response:** Array of journey objects.

## Get Records
- **Endpoint:** `/get_records`
- **Method:** GET
- **Description:** Retrieves all records from the database.
- **Response:** Array of record objects.

## Get Records by Car
- **Endpoint:** `/get_records_by_car`
- **Method:** GET
- **Description:** Retrieves records by car from the database.
- **Response:** Array of record objects.

## Get Records by Journey
- **Endpoint:** `/get_records_by_journey`
- **Method:** GET
- **Description:** Retrieves records by journey from the database.
- **Response:** Array of record objects.
