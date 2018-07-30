from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

#
# GENERAL SETTINGS
#

WSGI_APPLICATION = 'healthhouse.wsgi.application'

SECRET_KEY = os.environ['SECRET_KEY']

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

#
# STATIC FILES
#

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

#
# MEDIA FILES
#
