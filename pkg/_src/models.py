from pkg import db
from datetime import datetime
from pkg import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    user_image = db.Column(db.String(10), default='dafault-user-avatar.png', nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    acadimic_year = db.Column(db.String(50), default='اولى ثانوي')
    role = db.Column(db.String(15), default='تلميذ', nullable=False)
    is_approved = db.Column(db.Boolean, default=False, nullable=False)
    approve_request_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    is_user_request_rejected = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'User(id={self.id}, full_name="{self.full_name}", email="{self.email}", role="{self.role}")'
        

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    sender_id = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'Message(sender_id="{self.sender_id}", time="{self.time}", content="{self.content}")'