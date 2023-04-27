class User(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.Text, primary_key=True, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String)

    chats = db.relationship('Chat', secondary='user_chats', backref='users')

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



class Chat(db.Model):
    __tablename__ = 'chats'

    chat_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    chat_name = db.Column(db.Text, nullable=False)

    @classmethod
    def create_new_chat(cls, chat_name, chat_id):
        return cls(chat_name=chat_name, chat_id=chat_id)



class UserChat(db.Model):
    __tablename__ = 'user_chats'

    user_id = db.Column(db.Text, db.ForeignKey('users.username'), primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.chat_id'), primary_key=True)
