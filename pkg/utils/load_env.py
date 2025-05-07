from dotenv import load_dotenv
from os import getenv

load_dotenv()

SECRET_KEY = str(getenv('SECRET_KEY'))
SQLALCHEMY_DATABASE_URI = str(getenv('SQLALCHEMY_DATABASE_URI'))
SQLALCHEMY_TRACK_MODIFICATIONS = bool(getenv('SQLALCHEMY_TRACK_MODIFICATIONS'))
PRODUCTION = bool(getenv('PRODUCTION'))
GEMINI_API_KEY = getenv('GEMINI_API_KEY')


ADMIN_1_EMAIL = str(getenv('ADMIN_1_EMAIL'))
ADMIN_1_PASSWORD = str(getenv('ADMIN_1_PASSWORD'))

ADMIN_2_EMAIL = str(getenv('ADMIN_2_EMAIL'))
ADMIN_2_PASSWORD = str(getenv('ADMIN_2_PASSWORD'))
