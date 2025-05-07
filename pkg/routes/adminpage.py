
from flask import render_template, redirect, url_for, Blueprint
from flask_login import current_user, login_required
from pkg.utils.models import User
from pkg.utils.colors import *

adminpage_bp = Blueprint('adminpage', __name__)


@adminpage_bp.route('/adminpage', methods=['GET', 'POST'])
@login_required

def adminpage():

    def get_not_approved_users():
        return User.query.filter_by(is_approved=False, is_user_request_rejected=False).all()
    
    def get_approved_users():
        return User.query.filter_by(is_approved=True).all()
    
    if not current_user.role == 'مسؤول':
        return redirect(url_for('home.home'))

    
    return render_template('adminpage.html',
                         all_users = get_approved_users() + get_not_approved_users(),
                         approved_users = get_approved_users(),
                         not_approved_users = get_not_approved_users(),
                         )
                         
#! webSockest !#

from pkg.routes.Websockets.adminpage_ws import (
    handle_admin_delete_user_event  ,
    handle_admin_save_changes_event,
    handle_admin_pending_request_event
      )