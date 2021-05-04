"""
Django settings for IE104_SC project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import json

import dj_database_url

#Ubuntu Server configuration file



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['34.126.64.164', '127.0.0.1']

# '127.0.0.1'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    
    'news.apps.NewsConfig',
    'product.apps.ProductConfig',
    'accounts.apps.AccountsConfig',
    'brand.apps.BrandConfig',
    
    'django_filters',
    'bootstrap',
    'fontawesome',
    'django_icons',
    'storages',
    'multiselectfield',
    'django_summernote',
    'djrichtextfield',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # Caching whole page
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'IE104_SC.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'IE104_SC.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

""" SQLite3 database with localhost """

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

""" Localhost database through PgAdmin 4 - Postgres """
if 'RDS_HOSTNAME' in os.environ:
    SECRET_KEY = os.environ['BEAUTIF_SECRETKEY']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
elif 'RDS_HOSTNAME' in config:
    SECRET_KEY = config['SECRET_KEY']
    with open('/etc/config.json') as config_file:
        config = json.load(config_file)

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config['RDS_DB_NAME'],
            'USER': config['RDS_USERNAME'],
            'PASSWORD': config['RDS_PASSWORD'],
            'HOST': config['RDS_HOSTNAME'],
            'PORT': config['RDS_PORT'],
        }
    }
    AWS_ACCESS_KEY_ID = config['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = config['AWS_SECRET_ACCESS_KEY']
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# DATABASES['default'] = dj_database_url.config(conn_max_age=600)

""" Localhost database PostgresSQL on PgAdmin4 """

# Allocate database
AWS_S3_HOST = 'S3.ap-southeast-1.amazonaws.com'
AWS_S3_REGION_NAME = 'ap-southeast-1'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Staticfiles configuration

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIR = (
    os.path.join(BASE_DIR, 'static'),
)

# Media configuration

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
X_FRAME_OPTIONS = 'SAMEORIGIN'


LOGOUT_REDIRECT_URL = '/'

LOGIN_REDIRECT_URL = '/'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

DJANGO_ICONS = {
    "ICONS": {
        "edit": {"name": "far fa-pencil"},
    },
}

# S3 BUCKET CONFIG
AWS_STORAGE_BUCKET_NAME = 'beautifme'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Django Rich text field configuration
DJRICHTEXTFIELD_CONFIG = {
    'js': ['//cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': False,
        'plugins': 'link image table code',
        'toolbar': 'bold italic underline | link image | removeformat | formatselect | code',
        'width': 1200,
    },
    'profiles': {
        'basic': {
            'toolbar': 'bold italic | removeformat'
        },
        'advanced': {
            'plugins': 'link image table code',
            'toolbar': 'formatselect | bold italic | removeformat |'
            ' link unlink image table | code'
        }
    }
}

# Cache
CACHE = {
    'default' : {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
        'TIMEOUT': '4000',
        'OPTIONS': {
            'MAX_ENTRIES'
        }
    }
}

# Session Cache
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'