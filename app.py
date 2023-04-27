from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    # Do your authentication logic here
    if username == 'john' and password == 'pass':
        return jsonify({'success': True, 'message': 'Logged in successfully'})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'})



@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    # Do your validation logic here
    if not username:
        return jsonify({'success': False, 'message': 'Username is required'})
    if not password:
        return jsonify({'success': False, 'message': 'Password is required'})
    if not email:
        return jsonify({'success': False, 'message': 'Email is required'})
    # Add the user to the database
    # Return a success response
    return jsonify({'success': True, 'message': 'Registered successfully'})




if __name__ == '__main__':
    app.run(debug=True)