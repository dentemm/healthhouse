from .base import *

DEBUG = True

try:
    from .local import *
except ImportError:
    pass

#
# GENERAL SETTINGS
#

WSGI_APPLICATION = 'healthhouse.wsgi.application'

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.health-house.be', '.aws.amazon.com', '.herokuapp.com']

# Enforce SSL
SECURE_SSL_REDIRECT = True

#
# MIDDLEWARE
#

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

#
# DATABASE
#

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

#
# STATIC FILES
#

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#
# MEDIA FILES
#

AWS_STORAGE_BUCKET_NAME = 'hhwebsite'
# AWS_REGION = 'eu-central-1'
# AWS_S3_HOST = 's3.eu-central-1.amazonaws.com'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.eu-central-1.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'home.storage.custom_storages.MediaStorage'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
EMAIL_HOST= 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

NOCAPTCHA = True

RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']

MAILCHIMP_API_KEY = os.environ['MAILCHIMP_API_KEY']