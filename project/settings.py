import os
from dotenv import load_dotenv
import dj_database_url


load_dotenv()

DATABASES = {}

DATABASE_URL = os.environ['DATABASE_URL']

DATABASES["default"] = dj_database_url.parse(DATABASE_URL, conn_max_age=600)

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
