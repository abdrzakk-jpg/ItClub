from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField, EmailField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from pkg.utils.models import User
from flask_login import current_user
# Registration Form
class RegisterForm(FlaskForm):
    email = EmailField(
        'البريد الإلكتروني',
        validators=[
            DataRequired(message="البريد الإلكتروني مطلوب."),
            Email(message="الرجاء إدخال بريد إلكتروني صحيح."),
            Length(min=8,max=150)
        ],
        render_kw={"placeholder": "example@example.com"}
    )
    full_name = StringField(
        'الاسم بالكامل', 
        validators=[
            DataRequired(message="الاسم بالكامل مطلوب."),
            Length(min=2, max=20, message="الاسم يجب أن يكون بين 2 و 20 حرف.")
        ],
        render_kw={"placeholder": "اسمك الكامل مثلا - احمد مصطفى"}
    )
    birth_date = DateField(
        'تاريخ الازدياد',
        validators=[DataRequired(message="تاريخ الازدياد مطلوب.")]
    )

    role = SelectField(
        'هل أنت؟',
        choices=[
            'تلميذ',
            'استاذ',
            'مراقب'
        ],
        validators=[DataRequired(message="هذا الجزء مطلوب")],
        render_kw={
            "class": "w-full pr-11 pl-10 py-2 border-2 border-gray-300 text-gray-900 rounded-xl placeholder-gray-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition-all duration-200 hover:border-gray-300",
            "id":"roleSelect"
        }
    )
    academic_year = SelectField(
        'السنة الدراسية',
        choices=[
            'اولى ثانوي',
            'ثانية ثانوي',
            'ثالثة ثانوي'
        ],
        render_kw={
            "class": "w-full pr-11 pl-10 py-2 border-2 border-gray-300 text-gray-900 rounded-xl placeholder-gray-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition-all duration-200 hover:border-gray-300",
            "id":"acadimicYearSelect"
        }
    )


    password = PasswordField(
        'كلمة المرور', 
        validators=[
            DataRequired(message="كلمة المرور مطلوبة."),
            Length(min=5, max=30, message="كلمة المرور يجب أن تكون بين 5 و 30 حرف.")
        ], 
        render_kw={"placeholder": "كلمة المرور"}
    )
    submit = SubmitField('ارسال طلب انشاء الحساب')

# Login Form
class LoginForm(FlaskForm):
    email = EmailField(
        'البريد الإلكتروني',
        validators=[
            DataRequired(message="البريد الإلكتروني مطلوب."),
            Email(message="الرجاء إدخال بريد إلكتروني صحيح."),
            Length(min=8,max=150)
        ],
        render_kw={"placeholder": "example@example.com"}
    )
    password = PasswordField(
        'كلمة المرور', 
        validators=[
            DataRequired(message="كلمة المرور مطلوبة."),
            Length(min=5, max=30, message="كلمة المرور يجب أن تكون بين 5 و 30 حرف.")
        ],
        render_kw={"placeholder": "كلمة المرور"}
    )
    remember = BooleanField('تذكرني')
    submit = SubmitField('تسجيل الدخول')



    # Create forms for user profile update
class UpdateProfileForm(FlaskForm):
    full_name = StringField('الاسم الكامل', validators=[DataRequired()])
    email = EmailField('البريد الإلكتروني', validators=[DataRequired(), Email()])
    profile_picture = FileField('الصورة الشخصية', validators=[
        FileAllowed(['jpg', 'png', 'jpeg'], 'يسمح فقط بملفات الصور')
    ],
    render_kw={"id":"profile_picture"}
    )
    academic_year = SelectField(
        'السنة الدراسية',
        choices=[
            'اولى ثانوي',
            'ثانية ثانوي',
            'ثالثة ثانوي',
            
        ],
        render_kw={"id":"acadimicYearSelect"}
    )
    bio = TextAreaField('السيرة الذاتية', )

    submit = SubmitField('تحديث المعلومات')


class AiChatForm(FlaskForm):
    message = TextAreaField('راسل نبراس',id='message-value')
    submit = SubmitField('ارسال', id="send-message")