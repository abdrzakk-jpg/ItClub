
from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import login_user, current_user
from pkg.utils.forms import LoginForm
from pkg.utils.models import User
from pkg.utils.colors import *
from werkzeug.security import check_password_hash

login_bp = Blueprint('login', __name__)




@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    # initilaize Default Admin
    import pkg.utils.init_default_admins 
    
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))
    form = LoginForm() 

    if form.validate_on_submit():
        user = User.query.filter_by( email = form.email.data ).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                flash('مرحبا بعودتك', 'success')
                return redirect(url_for('home.home'))
            else:
                flash('يرجى التأكد من كلمة المرور', 'warn')
        else:
            flash('هذا المستخدم غير موجود', 'warn')
    return render_template('login.html', form=form)