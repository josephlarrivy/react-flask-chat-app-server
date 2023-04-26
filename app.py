from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='http://localhost:3000')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    message = f'{username} has joined the room {room}'
    emit('message', message, room=room)

@socketio.on('leave')
def handle_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    message = f'{username} has left the room {room}'
    emit('message', message, room=room)

@socketio.on('message')
def handle_message(data):
    username = data['username']
    room = data['room']
    message = data['message']
    emit('message', f'{username}: {message}', room=room)

if __name__ == '__main__':
    socketio.run(app)
