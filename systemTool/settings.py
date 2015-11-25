"""
Django settings for OpenRA Content Website project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b=jser_9!msujr9-%%jf410&kb=3dhnj0f5mvah45ws8q_%fau'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    # Required by allauth template tags
    "django.core.context_processors.request",
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'registration',
    'openraData',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'south',
    'corsheaders',
    'threadedcomments',
    'django.contrib.comments',
)

COMMENTS_APP = 'threadedcomments'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'systemTool.urls'

WSGI_APPLICATION = 'systemTool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

ACCOUNT_ACTIVATION_DAYS = 7


###########################
##### CUSTOM SETTINGS #####
###########################


# Path to directory where OpenRA versions are stored
OPENRA_ROOT_PATH = '/usr/local/openra/'

# OpenRA Versions matching their directory names
OPENRA_VERSIONS = {
    2: 'playtest-20150118',
    1: 'release-20141029',
    0: 'bleed', # just a name, see OPENRA_BLEED_PARSER setting
}

# Path to file which stores HASH of the latest `bleed` version
OPENRA_BLEED_HASH_FILE_PATH = ''

# `bleed` parser  directory is being updated by external script once new commit is pushed and has different structure (full path to directory)
OPENRA_BLEED_PARSER = ''


# Path to directory which will be shared over rsync, with full permissions for website user ( with slash at the end )
# Must be outside of website's path tree
# RSYNC_MAP_PATH: Website trigger will dump there 'good' maps for dedicated servers
RSYNC_MAP_PATH = ''

# Github related configuration
GITHUB_API_TOKEN = ''
GITHUB_USER = ''
GITHUB_REPO = ''

# Email address (FROM) in our custom mail methods
ADMIN_EMAIL_FROM = ''

# Email address (TO) in our custom mail methods, when informing admin
ADMIN_EMAIL_TO = ''

# Reply-to email address
DEFAULT_FROM_EMAIL = ''

# Determining amount of reports for item, required to forbid in-game downloading, synchronization with servers, etc.
REPORTS_PENALTY_AMOUNT = 3

# Is site under maintenance
SITE_MAINTENANCE = False
SITE_MAINTENANCE_OVER = '14:00 GMT' # when we finish technical works

# Time limit for some execution processes
UTILITY_TIME_LIMIT = 20

# HTTP_HOST of this site (ex: resource.openra.net)
HTTP_HOST = ''