
from flask_socketio import emit
from flask_login import login_required, current_user
from pkg import db, socketio, app
from pkg.utils.models import User
from pkg.utils.colors import *
from os import remove, path



@socketio.on('admin_save_changes_event')
@login_required
def handle_admin_save_changes_event(data):
    if not current_user.role == 'مسؤول':
        return
    try:
        user = User.query.filter_by(id=int(data[0])).first()
        if user:
            new_role = data[1]
            user.role = new_role
            db.session.commit()
            emit('admin_save_changes_respons', [user.id, user.role], broadcast=True)
    except Exception as e:
        db.session.rollback()
        print(f"Error saving admin changes: {str(e)}")


@socketio.on('admin_delete_user_event')
@login_required
def handle_admin_delete_user_event(data):
    if not current_user.role == 'مسؤول':
        return
    user = User.query.filter_by(id=int(data[0])).first()
    # yellow(path.join(app.root_path,'static/images/users/',current_user.user_image))
    user_image_path = path.join(app.root_path,'static/images/users/',current_user.user_image)
    if 'default-user-avatar.png' in user_image_path:
        pass
    else:
        remove(user_image_path)
    user.user_image = 'default-user-avatar.png'
    db.session.delete(user)
    db.session.commit() 

@socketio.on('admin_pending_request_event')
@login_required
def handle_admin_pending_request_event(data):
    if not current_user.role == 'مسؤول':
        return

    try:
        
        user = User.query.filter_by(id=int(data[0])).first()

        if not user:return

        if data[1]:
            if data[1].strip().lower() == 'reject':
                db.session.delete(user)

            if data[1].strip().lower() == 'accept':
                user.is_approved = True

        db.session.commit() 
    except Exception as e:
        db.session.rollback()
        red(f"Error:\nhandling admin request: {str(e)}")