# -*- coding: utf-8 -*-
import os
import django

DJANGO_ROOT     = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT       = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + "/..")

TEMPLATE_DIRS = (
    SITE_ROOT + '/templates/',
)

MEDIA_ROOT          = SITE_ROOT + '/media/'
MEDIA_URL           = '/media/'

STATIC_ROOT         = SITE_ROOT + '/static/'
STATIC_URL          = '/static/'

ADMIN_MEDIA_PREFIX  = '/static/admin/media/'

MESSAGE_STORAGE     = 'django.contrib.messages.storage.session.SessionStorage'

LOGIN_NOT_REQUIRED_PREFIXES = (
    '/login',
    '/media',
)
# Internationalization/localization stuff
USE_I18N = True
# USE_L10N = True

LANGUAGES = (
    ("en", u"English"),
    ("vi", u"Vietnamese"),
)

LOCALE_PATHS = (
    os.path.join(SITE_ROOT, 'locale'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware'
)

INSTALLED_APPS = (
    'apps.account',
    'apps.contact',
    'apps.intro',
    'apps.man',
    'apps.train',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.humanize',
)

TIME_ZONE            = 'Europe/Stockholm'
LANGUAGE_CODE        = 'en-us'
SITE_ID              = 1
USE_I18N             = True
ROOT_URLCONF         = 'urls'
LOGIN_URL            = '/login/'
AUTH_PROFILE_MODULE  = 'account.UserProfile'
INTERNAL_IPS         = ('192.168.0.188')
# DECIMAL_SEPARATOR    = ","
SYSTEM_USER_ID       = 1

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.csrf",
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

DEBUG = False

TEMPLATE_DEBUG       = False

# Add useful template tags
from django.template.loader import add_to_builtins
add_to_builtins("django.templatetags.i18n")
add_to_builtins("lib.utils")

'''
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211'
    }
}
'''

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        #"NAME": "giangday_moodledb",
        #"USER": "giangday_root",
        #"PASSWORD": "2tdp22ler@X",
        "NAME": "moodledb",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "3306",
    },
    "readonly": {
        "ENGINE": "django.db.backends.mysql",
        #"NAME": "giangday_moodledb",
        #"USER": "giangday_root",
        #"PASSWORD": "2tdp22ler@X",
        "NAME": "moodledb",
        "USER": "root",
        "PASSWORD": "root",        
        "HOST": "localhost",
        "PORT": "3306",
        "TEST_MIRROR": "default",
    },
}

AUTH_PROFILE_MODULE = 'accounts.UserProfile'