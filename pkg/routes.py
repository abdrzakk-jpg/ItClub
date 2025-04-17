from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from flask_socketio import emit
from pkg import app, db, socketio
from pkg._src.forms import LoginForm, RegisterForm, UpdateProfileForm, ChangeUserRoleForm
from pkg._src.models import User, Message
from pkg._src.helpers import calculate_age, hash_password, password_hash_checker, crypt_user_img_and_save_it, initilaize_default_admins
from pkg._src.colors import *
from datetime import datetime

# ======================= Base Route ======================= #

@app.route('/')
def home():
    try:
        if not current_user.is_anonymous:
            if current_user.role == 'مسؤول':
                current_user.is_approved = True
                db.session.commit()
            
            profile_pic = url_for('static', filename=f'images/users/{current_user.user_image}')
        else:
            profile_pic = url_for('static', filename=f'images/users/defaul-user-avatar.png')
        return render_template('home.html', title='Home Page', current_user=current_user,
                             profile_pic=profile_pic)
    except Exception as e:
        print(f"Error in home route: {str(e)}")
        return render_template('error.html')

# ======================= Auth Routes ======================= #

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if password_hash_checker(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                flash('مرحبا بعودتك', 'success')
                return redirect(url_for('home'))
            else:
                print(f'{g}{user.password, form.password.data}{re}')
                flash('يرجى التأكد من كلمة المرور', 'warn')
        else:
            flash('هذا المستخدم غير موجود', 'warn')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        rejected_users = User.query.filter_by(is_user_request_rejected=True)

        # age verification
        if calculate_age(form.birth_date.data) < 15:
            flash('عمرك يجب ان يفوق 15 سنة')
        elif rejected_users.filter_by(email=form.email.data).first():
            flash('للأسف تم رفض طلبك من احد المسؤولين, يرجى التوجه لأقرب مسؤول والاستفسار عن سبب الرفض', 'warn')
        else:
            try:
                new_user = User(
                    email=form.email.data,
                    full_name=form.full_name.data,
                    password=hash_password(form.password.data),
                    birth_date=form.birth_date.data,
                    acadimic_year=form.acadimic_year.data if form.role.data == 'تلميذ' else form.role.data,
                    role=form.role.data,
                    is_approved=False
                )
                db.session.add(new_user)
                db.session.commit()
                flash('سيتم أخذ طلبك بعين الاعتبار يرجى الانتظار حتى موافقة المسؤولين و يرجى تسجيل الدخول لتأكيد معلوماتك', 'success')
                return redirect(url_for('login'))
            except Exception as e:
                db.session.rollback()
                flash('حدث خطأ أثناء التسجيل. يرجى المحاولة مرة أخرى.', 'error')
                print(f"Registration error: {str(e)}")

    return render_template('register.html', register_form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# ======================= Account Routes ======================= #

@app.route('/myaccount', methods=['GET', 'POST'])
@login_required
def myaccount():
    form = UpdateProfileForm()
    
    try:
        if form.validate_on_submit():
            current_user.full_name = form.full_name.data
            current_user.email = form.email.data
            
            if form.profile_picture.data:
                current_user.user_image = crypt_user_img_and_save_it(form.profile_picture.data)

            db.session.commit()
            flash('تم تحديث معلوماتك بنجاح', 'success')
            return redirect(url_for('myaccount'))
        
        elif request.method == 'GET':
            form.full_name.data = current_user.full_name
            form.email.data = current_user.email

        profile_pic = url_for('static', filename=f'images/users/{current_user.user_image}')
        return render_template('myaccount.html', form=form, current_user=current_user,
                             profile_pic=profile_pic)
    except Exception as e:
        db.session.rollback()
        print(f"Error in myaccount route: {str(e)}")
        flash('حدث خطأ أثناء تحديث الحساب', 'error')
        return redirect(url_for('home'))

# ======================= Chat Routes ======================= #

@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    if not current_user.is_approved:
        flash('يجب الموافقة على حسابك قبل الانضمام الى الدردشة', 'warn')
        return redirect(url_for('home'))
    
    try:
        online_users = []
        for user in User.query.all():
            if user.is_active:
                online_users.append(user)

        messages = Message.query.order_by(Message.time.asc()).all()
        print(f'{g}{messages}{re}')
        profile_pic = url_for('static', filename=f'images/users/{current_user.user_image}')
        users_filterby = User.query.filter_by
        return render_template('chat.html', messages=messages, current_user=current_user,
                             online_users=online_users, profile_pic=profile_pic,
                             users_filterby=users_filterby)
    except Exception as e:
        print(f"Error in chat route: {str(e)}")
        flash('حدث خطأ أثناء تحميل الدردشة', 'error')
        return redirect(url_for('home'))

@socketio.on('message_event')
@login_required
def handle_message(data):
    try:
        current_time = datetime.now()
        
        print(f'{r}{data}{re}')
        
        newMessage = Message(
            content = data['message'],
            sender_id = current_user.id,
            time = current_time
        )
        db.session.add(newMessage)
        db.session.commit()
        
        message_data = {
            "message": data['message'],
            "sender_id": current_user.id,
            "sender_name": current_user.full_name,
            "user_image": current_user.user_image,
            "timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f'{r}{message_data}{re}')
        emit('message_res', message_data, broadcast=True)
    except Exception as e:
        db.session.rollback()
        print(f"Error handling message: {str(e)}")

# ======================= Admin Routes ======================= #

@app.route('/adminpage', methods=['GET', 'POST'])
@login_required
def adminpage():
    if not current_user.role == 'مسؤول':
        flash('غير مصرح لك بالدخول', 'error')
        return redirect(url_for('home'))

    form = ChangeUserRoleForm()
    not_approved_users = User.query.filter_by(is_approved=False, is_user_request_rejected=False).all()
    all_users = User.query.all()
    filter_by = User.query.filter_by
    approved_users = User.query.filter_by(is_approved=True).all()
    rejected_users = User.query.filter_by(is_user_request_rejected=True).all()
    return render_template('adminpage.html',
                         all_users=all_users,
                         filter_by=filter_by,
                         not_approved_users=not_approved_users,
                         approved_users=approved_users,
                         rejected_users=rejected_users,
                         form=form)

@socketio.on('admin_pending_request_handler_event')
@login_required
def handle_admin_pending_request_handler_event(data):
    if not current_user.role == 'مسؤول':
        return

    try:
        emit('res', {"msg": data}, broadcast=True)
        user = User.query.filter_by(id=int(data[0])).first()
        if not user:
            return

        if data[1]:
            if data[1] == 'reject':
                db.session.delete(user)
            if data[1] == 'accept':
                user.is_approved = True
            if data[1] == 'ignore':
                user.is_approved = False
                user.is_user_request_rejected = True

        db.session.commit()
        print(f'{r}{data}{re}')
    except Exception as e:
        db.session.rollback()
        print(f"Error handling admin request: {str(e)}")

@socketio.on('admin_save_changes_event')
@login_required
def handle_admin_save_changes_event(data):
    try:
        user = User.query.filter_by(id=int(data[0])).first()
        if user:
            new_role = data[1]
            user.role = new_role
            db.session.commit()
            emit('admin_save_changes_respons', [user.id, user.role])
            print(f'{g}{data[0], data[1]}{re}')
    except Exception as e:
        db.session.rollback()
        print(f"Error saving admin changes: {str(e)}")