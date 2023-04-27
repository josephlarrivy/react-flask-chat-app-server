from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class AddUserForm(FlaskForm):
    """user registration"""
    username = StringField('Username', validators=[InputRequired(), Length(min=10)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8)])
    email = StringField('email', validators=[InputRequired(), Email()])


class CreateChatForm(FlaskForm):
    """name and create a chat"""
    chat_name = StringField('Chat Name', validators=[InputRequired()])