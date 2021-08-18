import os
import dj_database_url
import environ


env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, [])
)
env.read_env(env.str('./', '.env'))

DEBUG = env('DEBUG')

DATABASES = {}

DATABASE_URL = env('DATABASE_URL')

DATABASES["default"] = dj_database_url.parse(DATABASE_URL, conn_max_age=600)

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('SECRET_KEY')

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS: list[str] = env('ALLOWED_HOSTS')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = env('LANGUAGE_CODE')

TIME_ZONE = env('TIME_ZONE')

USE_TZ = True
