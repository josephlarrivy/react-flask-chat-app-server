from flask import Flask, jsonify, request
from flask_cors import CORS
from Models import connect_db, db, User, ChatName, UserChat
from forms import AddUserForm, CreateChatForm
from sqlalchemy import desc, delete
from sqlalchemy.exc import IntegrityError
import random

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///chat-app-database"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["SECRET_KEY"] = "W8ddvewdd@$hdj"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)



@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username:
        return jsonify({'success': False, 'message': 'Username is required'})
    if not password:
        return jsonify({'success': False, 'message': 'Password is required'})
    if not email:
        return jsonify({'success': False, 'message': 'Email is required'})

    new_user = User.register_new_user(username, password, email)
    db.session.add(new_user)

    try:
        db.session.commit()
    except IntegrityError:
        return jsonify({'success': False, 'message': 'Username is already taken'})


    return jsonify({'success': True, 'message': 'Registered successfully'})



@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username:
        return jsonify({'success': False, 'message': 'Username is required'})
    if not password:
        return jsonify({'success': False, 'message': 'Password is required'})

    user = User.authenticate(username, password)

    if user:
        return jsonify({'success': True, 'message': 'Login success'})
    else:
        return jsonify({'success': False, 'message': 'Login not success'})




@app.route('/createChat', methods=['POST'])
def create_chat():
    data = request.json
    chat_name = data.get('chatname')

    if not chat_name:
        return jsonify({'success': False, 'message': 'Username is required'})

    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    num3 = random.randint(100, 999)

    chat_id = f"{num1}-{num2}-{num3}"

    chat = ChatName.create_new_chat(chat_name, chat_id)
    db.session.add(chat)

    try:
        db.session.commit()
    except IntegrityError:
        return jsonify({'success': False, 'message': 'could not create chat'})


    return jsonify({'success': True, 'message': 'Registered successfully'})




if __name__ == '__main__':
    app.run(debug=True)