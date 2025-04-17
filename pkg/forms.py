from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import FileRequired, FileAllowed

class LoginForm(FlaskForm):
    email = StringField('البريد الإلكتروني', validators=[DataRequired(), Email()],
                       render_kw={"class": "form-control", "placeholder": "أدخل بريدك الإلكتروني"})
    password = PasswordField('كلمة المرور', validators=[DataRequired()],
                           render_kw={"class": "form-control", "placeholder": "أدخل كلمة المرور"})
    submit = SubmitField('تسجيل الدخول',
                        render_kw={"class": "btn btn-primary w-100"})

class RegisterForm(FlaskForm):
    full_name = StringField('الاسم الكامل', validators=[DataRequired(), Length(min=4, max=50)],
                          render_kw={"class": "form-control", "placeholder": "أدخل اسمك الكامل"})
    email = StringField('البريد الإلكتروني', validators=[DataRequired(), Email()],
                       render_kw={"class": "form-control", "placeholder": "أدخل بريدك الإلكتروني"})
    password = PasswordField('كلمة المرور', validators=[DataRequired(), Length(min=6)],
                           render_kw={"class": "form-control", "placeholder": "أدخل كلمة المرور"})
    confirm_password = PasswordField('تأكيد كلمة المرور', 
                                   validators=[DataRequired(), EqualTo('password', message='كلمات المرور غير متطابقة')],
                                   render_kw={"class": "form-control", "placeholder": "أعد إدخال كلمة المرور"})
    birth_date = DateField('تاريخ الميلاد', validators=[DataRequired()],
                          render_kw={"class": "form-control", "type": "date"})
    user_image = FileField('الصورة الشخصية', 
                          validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'الصور فقط!')],
                          render_kw={"class": "form-control"})
    submit = SubmitField('إنشاء حساب',
                        render_kw={"class": "btn btn-primary w-100"})

class UpdateAccountForm(FlaskForm):
    full_name = StringField('الاسم الكامل', validators=[DataRequired(), Length(min=4, max=50)],
                          render_kw={"class": "form-control", "placeholder": "أدخل اسمك الكامل"})
    email = StringField('البريد الإلكتروني', validators=[DataRequired(), Email()],
                       render_kw={"class": "form-control", "placeholder": "أدخل بريدك الإلكتروني"})
    birth_date = DateField('تاريخ الميلاد', validators=[DataRequired()],
                          render_kw={"class": "form-control", "type": "date"})
    user_image = FileField('تحديث الصورة الشخصية',
                          validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'الصور فقط!')],
                          render_kw={"class": "form-control"})
    current_password = PasswordField('كلمة المرور الحالية',
                                   render_kw={"class": "form-control", "placeholder": "أدخل كلمة المرور الحالية"})
    new_password = PasswordField('كلمة المرور الجديدة',
                               render_kw={"class": "form-control", "placeholder": "أدخل كلمة المرور الجديدة"})
    confirm_new_password = PasswordField('تأكيد كلمة المرور الجديدة',
                                       validators=[EqualTo('new_password', message='كلمات المرور غير متطابقة')],
                                       render_kw={"class": "form-control", "placeholder": "أعد إدخال كلمة المرور الجديدة"})
    submit = SubmitField('تحديث المعلومات',
                        render_kw={"class": "btn btn-primary"})

class AdminForm(FlaskForm):
    change_role = SelectField('تغيير الدور',
                            choices=[('تلميذ', 'تلميذ'), ('استاذ', 'أستاذ'), ('مراقب', 'مراقب'), ('مسؤول', 'مسؤول')],
                            render_kw={"class": "form-select"})
    submit = SubmitField('حفظ التغييرات',
                        render_kw={"class": "btn btn-primary"}) 