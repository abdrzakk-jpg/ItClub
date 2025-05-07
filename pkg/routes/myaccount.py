
from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import current_user, login_required, logout_user
from pkg import db
from pkg.utils.forms import UpdateProfileForm
from pkg.utils.helpers import crypt_user_img_and_save_it
from pkg.utils.colors import *

myaccount_bp = Blueprint('myaccount', __name__)

# @cached_property
@myaccount_bp.route('/myaccount', methods=['GET', 'POST'])
@login_required
def myaccount():
    form = UpdateProfileForm()
    try:
        if form.validate_on_submit():
            current_user.full_name = form.full_name.data
            current_user.email = form.email.data
            current_user.academic_year = form.academic_year.data
            current_user.bio = form.bio.data
            
            if form.profile_picture.data:
                current_user.user_image = crypt_user_img_and_save_it(form.profile_picture.data)

            green('ACCOUNT UPDATED')

            db.session.commit()
            print(current_user.user_image)
            
            flash('تم تحديث معلوماتك بنجاح', 'success')

            return redirect(url_for('myaccount.myaccount'))
        elif request.method == 'GET':
            form.full_name.data = current_user.full_name
            form.email.data = current_user.email
            form.academic_year.data = current_user.academic_year
            form.bio.data = current_user.bio
        else:
            red(f'myaccount Error:\n{form.errors}')
        return render_template( 'myaccount.html', form=form, current_user=current_user )
    except Exception as e:
        db.session.rollback()
        red(f"Error in myaccount route:\n{str(e)}/{str(e.with_traceback())}")
        flash('حدث خطأ أثناء تحديث الحساب', 'error')
        return redirect(url_for('home.home'))



@myaccount_bp.route('/logout')
def logout():
    logout_user()
    session.clear()
    resp = redirect(url_for('login.login'))
    resp.delete_cookie('session')
    return resp
