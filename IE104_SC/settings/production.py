from IE104_SC.settings.base import *

# Override base.py

ALLOWED_HOSTS = ['34.126.64.164', 'beautifme.com', '.beautifme.com']

DEBUG = False

SECURE_SSL_REDIRECT = True

with open('/etc/config.json') as config_file:
        config = json.load(config_file)

SECRET_KEY = config['SECRET_KEY']

INSTALLED_APPS += [
    "google_analytics",
]

# MIDDLEWARE += [
#     # Google Analytics
#     'google_analytics.middleware.GoogleAnalyticsMiddleware',   
# ]

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

# Google Analytics
GOOGLE_ANALYTICS = {
    'google_analytics_id': 'G-RBDFR7443J',
}

# Celery
# CELERY_IMPORTS = ('google_analytics.tasks')
# GOOGLE_ANALYTICS_IGNORE_PATH = ['/account/', '/admin/', ]