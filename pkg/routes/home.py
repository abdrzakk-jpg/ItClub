
from flask import render_template, Blueprint
from flask_login import current_user
from pkg import db
from pkg.utils.colors import *
home_bp = Blueprint('home', __name__)
# ======================= Base Route ======================= #
@home_bp.route('/')
def home():
    try:
        if not current_user.is_anonymous and current_user.role == 'مسؤول':
            current_user.is_approved = True
            db.session.commit()
            
        return render_template('home.html', current_user=current_user,
                             )
    except ValueError as e:
        print(f"Error in home route: {str(e)}")
        return render_template('error.html')
    
