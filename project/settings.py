import os
import environ


env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
)
env.read_env(env.str('./', '.env'))

DEBUG = env('DEBUG')

DATABASES = {}

DATABASES["default"] = env.db(
    'DATABASE_URL', default="postgres://user:password@domain.yourdomain.org:5434/yourdatabase")

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
