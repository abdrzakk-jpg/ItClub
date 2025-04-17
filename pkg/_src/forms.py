from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, DateField,EmailField
from flask_wtf.file import FileAllowed, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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
    acadimic_year = SelectField(
        'السنة الدراسية',
        choices=[
            'اولى ثانوي',
            'ثانية ثانوي',
            'ثالثة ثانوي'
        ],
        render_kw={
            "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            "id":"acadimicYearSelect"
        }
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
            "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            "id":"roleSelect"
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
    ])
    acadimic_year = SelectField(
        'السنة الدراسية',
        choices=[
            'اولى ثانوي',
            'ثانية ثانوي',
            'ثالثة ثانوي'
        ],
        validators=[DataRequired(message="السنة الدراسية مطلوبة.")],
        render_kw={
            "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            "id":"acadimicYearSelect"
        }
    )
    submit = SubmitField('تحديث المعلومات')



class ChangeUserRoleForm(FlaskForm):
    change_role =  SelectField(
        'نوع المستخدم',
        choices=[
            'تلميذ',
            'استاذ',
            'مراقب',
            'مسؤول'
        ],
        render_kw={
            "class": "appearance-none bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            "id":"changeRoleSelect"
        }
    )
    submit = SubmitField('تحديث المعلومات')