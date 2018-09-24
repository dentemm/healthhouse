from .base import *

DEBUG = True

try:
    from .local import *
except ImportError:
    pass

#
# GENERAL SETTINGS
#

# INSTALLED_APPS = INSTALLED_APPS + [
#     'wagtail.contrib.postgres_search',
# ]

WSGI_APPLICATION = 'healthhouse.wsgi.application'

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.health-house.be', '.aws.amazon.com', '.herokuapp.com']

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

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

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


#
# SEARCH
#

# WAGTAILSEARCH_BACKENDS = {
#     'default': {
#         'BACKEND': 'wagtail.contrib.postgres_search.backend',
#         # PS: dutch also exists: https://stackoverflow.com/questions/39751892/get-full-list-of-full-text-search-configuration-languages
#         'SEARCH_CONFIG': 'english',
#         'ATOMIC_REBUILD': True
#     }
# }

#
# MAILING FUNCTIONALITY
#

EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
EMAIL_HOST= 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
