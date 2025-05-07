from flask import url_for
from flask_socketio import emit
from flask_login import current_user, login_required
from pkg import db, socketio
from pkg.utils.models import Message
# from pkg.utils.colors import *
from datetime import datetime


#! webSockets !#
@socketio.on('message_event')
@login_required
def handle_message(data):
    try:
        current_time = datetime.now()
        
        newMessage = Message(
            content = data['message'],
            sender_name = data['sender_name'],
            time = current_time
        )
        db.session.add(newMessage)
        db.session.commit()
        
        message_data = {
            "message": data['message'],
            "sender_id": current_user.id,
            "sender_name": current_user.full_name,
            "user_image": url_for('static', filename='images/users/'+current_user.user_image),
            "timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        emit('message_res', message_data, broadcast=True)
    except Exception as e:
        db.session.rollback()
        print(f"Error handling message: {str(e)}")
