
from flask import render_template, redirect, url_for, flash, Blueprint, request
from flask_login import current_user, login_required
from pkg import db
from pkg.utils.models import Message, User
from pkg.utils.colors import *
from datetime import datetime, timedelta

chat_bp = Blueprint('chat', __name__)



@chat_bp.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    if not current_user.is_approved:
        flash('يجب الموافقة على حسابك قبل الانضمام الى الدردشة', 'warn')
        return redirect(url_for('home.home'))
    try:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

        def get_online_users():
            five_minutes_ago = datetime.now() - timedelta(minutes=5)
            return User.query.filter(
                User.last_seen >= five_minutes_ago,
                User.is_approved == True
            ).all()

        messages = Message.query.order_by(Message.time.asc()).all()
        online_users = get_online_users()
        
        def get_sender_user_image(name):
            user = User.query.filter_by(full_name=name).first()
            if user and user.user_image:
                return url_for('static', filename='images/users/' + user.user_image)
            return url_for('static', filename='images/users/default-user-avatar.png')
                
        return render_template('chat.html', 
                             messages=messages, 
                             current_user=current_user,
                             online_users=online_users,
                             get_sender_user_image=get_sender_user_image 
                             )
    except Exception as e:
        red(f"Error in chat route:\n{str(e)}/{str(e.with_traceback())}")
        db.session.rollback()
        flash('حدث خطأ أثناء تحميل الدردشة', 'error')
        return redirect(url_for('home.home'))

from pkg.routes.Websockets.chat_ws import handle_message