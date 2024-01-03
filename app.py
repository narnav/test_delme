from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (in-memory storage)
users = [
    {"id": 1, "age": 25, "email": "user1@example.com"},
    {"id": 2, "age": 30, "email": "user2@example.com"}
]
next_id = 3  # ID counter for new users

# Routes for CRUD operations

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Get a specific user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.json
    new_user = {
        "id": next_id,
        "age": data.get('age'),
        "email": data.get('email')
    }
    users.append(new_user)
    next_id += 1
    return jsonify(new_user), 201

# Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        data = request.json
        user['age'] = data.get('age', user['age'])
        user['email'] = data.get('email', user['email'])
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'message': 'User deleted'})

if __name__ == '__main__':
    app.run(debug=True)
