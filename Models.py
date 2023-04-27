from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.Text, primary_key=True, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String)

    chats = db.relationship('ChatName', secondary='user_chatnames', backref='users')

    @classmethod
    def register_new_user(cls, username, password, email):
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode('utf8')
        return cls(username=username, password=hashed_utf8, email=email)

    @classmethod
    def authenticate(cls, username, password):
        u = User.query.filter_by(username=username).first()
        if u and bcrypt.check_password_hash(u.password, password):
            return u
        else:
            return False






class ChatName(db.Model):
    __tablename__ = 'chatnames'

    chat_id = db.Column(db.Text, unique=True, primary_key=True, nullable=False)
    chat_name = db.Column(db.Text, nullable=False)
    chat_owner = db.Column(db.Text, db.ForeignKey('users.username'), nullable=False)
    
    owner = db.relationship('User', backref='owned_chats', foreign_keys=[chat_owner])

    @classmethod
    def create_new_chat(cls, chat_name, chat_id, chat_owner):
        return cls(chat_name=chat_name, chat_id=chat_id, chat_owner=chat_owner)









class UserChat(db.Model):
    __tablename__ = 'user_chatnames'

    user_id = db.Column(db.Text, db.ForeignKey('users.username'), primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chatnames.chat_id'), primary_key=True)
