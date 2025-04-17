from datetime import date, datetime
from pkg import bcrypt
from flask_login import current_user
from PIL import Image
import os
from pkg import *
from werkzeug.utils import secure_filename
from secrets import token_hex
from pkg._src.colors import *
from pkg import db
from pkg._src.models import User
from flask_login import login_user


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# hash password to add more security
def hash_password(password) -> str:
    return bcrypt.generate_password_hash(password).decode('utf-8')

# check if the given password is equal to the hashed version of password
def password_hash_checker(hash_password, password) -> bool: return bcrypt.check_password_hash(hash_password, password)



def crypt_user_img_and_save_it(file):
    picture_file = secure_filename(file.filename)
    _, file_ex = picture_file.rsplit('.',1)
    print(c ,file_ex, re)
    # Create a unique filename with timestamp
    filename = f"{token_hex(16)}.{file_ex}"
    # Save the file
    picture_path = os.path.join(app.root_path, 'static/images/users', filename)
    os.makedirs(os.path.dirname(picture_path), exist_ok=True)
    # Resize and save the image
    output_size = (150, 150)
    i = Image.open(file)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return filename


def initilaize_default_admins(full_name, email, password, birth_date, acadimic_year):
    user = User.query.filter_by(email = email).first()
    if user:
        print(f'{lr}[{email}]{r}This User Already Exists, Skipping....{re}')
    else:
        new_admin = User(
            full_name = full_name,
            email = email,
            password = hash_password(password),
            birth_date = birth_date,
            acadimic_year = acadimic_year,
            role = 'مسؤول',
            is_approved = True
        )
        db.session.add(new_admin)
        db.session.commit()