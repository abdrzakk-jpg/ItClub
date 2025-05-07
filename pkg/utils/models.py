from pkg import db
from datetime import datetime
from pkg import login_manager
from flask_login import UserMixin
from pkg.utils.colors import *


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, index=True)
    full_name = db.Column(db.String(100), index=True)
    password = db.Column(db.String(60))
    birth_date = db.Column(db.Date)
    academic_year = db.Column(db.String(20))
    bio = db.Column(db.Text)
    role = db.Column(db.String(20), index=True)
    user_image = db.Column(db.String(20), default='default-user-avatar.png')
    is_approved = db.Column(db.Boolean, default=False, index=True)
    is_user_request_rejected = db.Column(db.Boolean, default=False, index=True)
    approve_request_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, index=True)
    last_seen = db.Column(db.DateTime)

    # aichats = db.relationship('AiChat', backref='user', lazy=True)

    def __repr__(self):
        return f'User({self.full_name}, {self.email})'

            
# TO THE NEXT UPDATE
# class AiChat(db.Model):
#     __tablename__ = 'ai_chat'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     messages = db.relationship('AiChatMessage', backref='chat', lazy=True)

#     def __repr__(self):
#         return f'AiChat(id="{self.id}",user_id="{self.user_id}")'


# class AiChatMessage(db.Model):
#     __tablename__ = 'ai_message'

#     id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
#     question = db.Column(db.Text, nullable=False)
#     ai_answer = db.Column(db.Text, default=None, nullable=True)
#     chat_id = db.Column(db.Integer, db.ForeignKey('ai_chat.id'), nullable=False)

#     def __repr__(self):
#         return f'AiChatMessage(messageID="{self.id}",chatID="{self.chat_id}")'
    

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    sender_name = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, index=True)
    def __repr__(self) -> str:
        return f'Message(sender_name="{self.sender_name}", time="{self.time}", content="{self.content}")'
    
