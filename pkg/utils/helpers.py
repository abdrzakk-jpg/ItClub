from datetime import date
from PIL import Image
import os
from pkg import *
from werkzeug.utils import secure_filename
from secrets import token_hex
from pkg.utils.colors import *
from pkg import app
from pkg.utils.models import User
from werkzeug.security import generate_password_hash


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def crypt_user_img_and_save_it(file):
    picture_file = secure_filename(file.filename)
    _, file_ex = picture_file.rsplit('.',1)
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





def initilaize_default_admin(full_name, email, password, birth_date, academic_year):
    user = User.query.filter_by(email = email).first()
    if user:
        red(f'[{email}]This User Already Exists, Skipping....')
    else:
        new_admin = User(
            full_name = full_name,
            email = email,
            password = generate_password_hash(password),
            birth_date = birth_date,
            academic_year = academic_year,
            role = 'مسؤول',
            is_approved = True
        )
        db.session.add(new_admin)
        db.session.commit()
