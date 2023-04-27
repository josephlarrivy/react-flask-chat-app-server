import os
from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/socket.io/')
def handle_socketio_polling():
    transport = request.args.get('transport')
    polling_id = request.args.get('t')
    
    if transport == 'polling' and polling_id:
        response_data = '96:0{"sid":"dummy_sid","upgrades":[],"pingInterval":25000,"pingTimeout":5000}'
        response = Response(response_data, content_type='text/plain')
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    
    return 'Not Found', 404


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

@socketio.on('owner_leave')
def handle_owner_leave(room):
    emit('message', {'text': 'The owner has left the chat. You have been disconnected.'}, room=room)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5002))
    socketio.run(app, port=port)
