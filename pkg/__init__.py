from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_login import LoginManager
from pkg.utils.load_env import SECRET_KEY, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS



app = Flask(__name__)

db = SQLAlchemy()
socketio = SocketIO()
login_manager = LoginManager()

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS


db.init_app(app)
socketio.init_app(app)
login_manager.init_app(app)

# Configure login manager
login_manager.login_message = 'يجب عليك تسجيل الدخول اولا'
login_manager.login_view = '/login'
login_manager.login_message_category = 'info'



# register blueprints
from pkg.routes import all_bps
for bp in all_bps:
    app.register_blueprint(bp)


# create db
with app.app_context():
    db.create_all()

