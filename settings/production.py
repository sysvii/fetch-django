import os

from .defaults import *

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = os.environ['DJANGO_FETCH_SECRET_KEY']

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DJANGO_FETCH_POSTGRES_DB_NAME'],
        'USER': os.environ['DJANGO_FETCH_POSTGRES_USER'],
        'PASSWORD': os.environ['DJANGO_FETCH_POSTGRES_PASS'],
        'HOST': os.environ['DJANGO_FETCH_POSTGRES_HOST'],
        'PORT': os.environ['DJANGO_FETCH_POSTGRES_PORT'],
    }
}
