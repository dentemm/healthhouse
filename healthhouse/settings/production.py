from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

SECRET_KEY = os.environ['SECRET_KEY']

#
# DATABASE SETUP
#

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthhouse'
    }
}

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

#
# STATIC FILES
#

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

#
# MEDIA FILES
#
