# Flask CRUD Application - User Management

This Flask application serves as a simple CRUD (Create, Read, Update, Delete) API for managing user data including age and email.

## Features

- **Create**: Add a new user with age and email.
- **Read**: Retrieve all users or fetch a specific user by ID.
- **Update**: Modify user details (age, email) based on user ID.
- **Delete**: Remove a user from the system by ID.

## Installation

1. Ensure you have Python 3 installed.
2. Clone this repository: `git clone https://github.com/yourusername/flask-crud-app.git`
3. Navigate to the project directory: `cd flask-crud-app`
4. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. The server will start running on `http://127.0.0.1:5000/`.
3. Use API endpoints to perform CRUD operations:

    - **GET /users**: Get all users.
    - **GET /users/<user_id>**: Get a specific user by ID.
    - **POST /users**: Create a new user (Send JSON payload with age and email).
    - **PUT /users/<user_id>**: Update a user by ID (Send JSON payload with age and/or email).
    - **DELETE /users/<user_id>**: Delete a user by ID.

## Sample JSON Payload

For creating or updating a user, use JSON data in the following format:

```json
{
    "age": 30,
    "email": "user@example.com"
}
