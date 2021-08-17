import os
from dotenv import load_dotenv
import dj_database_url


load_dotenv()

DATABASES = {
    'default': {
        'DB_ENGINE': os.environ['DB_ENGINE'],
        'DB_HOST': os.environ['DB_HOST'],
        'DB_PORT': os.environ['DB_PORT'],
        'DB_NAME': os.environ['DB_NAME'],
        'DB_USER': os.environ['DB_USER'],
        'DB_PASSWORD': os.environ['DB_PASSWORD'],
    }
}

DATABASES['default'] = dj_database_url.parse('postgres://...', conn_max_age=600)

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = os.environ["DEBUG"]

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


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
