from IE104_SC.settings.base import *

# Override base.py

ALLOWED_HOSTS = ['34.126.64.164', 'beautifme.com', '.beautifme.com']

DEBUG = False

with open('/etc/config.json') as config_file:
        config = json.load(config_file)

SECRET_KEY = config['SECRET_KEY']

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