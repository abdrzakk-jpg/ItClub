
from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import current_user
from pkg import db
from pkg.utils.helpers import calculate_age
from pkg.utils.forms import RegisterForm
from pkg.utils.models import User
from pkg.utils.colors import *
from werkzeug.security import generate_password_hash



register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))
    form = RegisterForm()
    if form.validate_on_submit():

        # TODO: Come Back And Edit It
        # rejected_users = User.query.filter_by(is_user_request_rejected=True).all()

        # age verification
        if calculate_age(form.birth_date.data) < 15:
            flash('عمرك يجب ان يفوق 15 سنة')

        else:
            try:
                new_user = User(
                    email=form.email.data,
                    full_name=form.full_name.data,
                    password=generate_password_hash(form.password.data),
                    birth_date=form.birth_date.data,
                    academic_year=form.academic_year.data if form.role.data == 'تلميذ' else form.role.data,
                    role=form.role.data,
                    is_approved=False
                )
                db.session.add(new_user)
                db.session.commit()
                flash('سيتم أخذ طلبك بعين الاعتبار يرجى الانتظار حتى موافقة المسؤولين', 'success')
                return redirect(url_for('login.login'))
            except Exception as e:
                db.session.rollback()
                flash('حدث خطأ أثناء التسجيل. يرجى المحاولة مرة أخرى.', 'error')
                red(f"Registration error:\n{str(e)}")

    return render_template('register.html', register_form=form)
