import os
from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.register_blueprint(sockets)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = data['room']
    join_room(room)

    message = f'{username} has joined the room'

    message_dict = {'username': username, 'message': message}
    emit('message', message_dict, room=room)

@socketio.on('leave')
def handle_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)

    message = f'{username} has left the room'

    message_dict = {'username': username, 'message': message}
    emit('message', message_dict, room=room)

@socketio.on('message')
def handle_message(data):
    username = data['username']
    room = data['room']
    message = data['message']

    message_dict = {'username': username, 'message': message}
    emit('message', message_dict, room=room)


if __name__ == '__main__':
    socketio.run(app)