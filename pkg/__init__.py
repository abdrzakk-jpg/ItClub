from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy()
bcrypt = Bcrypt(app)
socketio = SocketIO(app)
login_manager = LoginManager(app)

app.config['SECRET_KEY'] = '7636add441568ae13c5c8a33e0f4b38f2299c4ed0a300ede799c803a44bb66f1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure login manager
login_manager.login_message = 'يجب عليك تسجيل الدخول اولا'
login_manager.login_view = '/login'
login_manager.login_message_category = 'info'
