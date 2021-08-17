import os
from dotenv import load_dotenv
import dj_database_url


load_dotenv()

DATABASES = {}

database_url = f"postgres://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"

DATABASES["default"] = dj_database_url.parse(database_url, conn_max_age=600)

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = os.environ["LOG_LEVEL"]

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]"]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = os.environ['LANGUAGE_CODE']

TIME_ZONE = os.environ['TIME_ZONE']

USE_TZ = True
