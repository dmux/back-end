# -*- coding: utf-8 -*-
import os
from datetime import timedelta
from configurations import Configuration, values
from django.contrib.messages import constants as messages
from dotenv import load_dotenv

load_dotenv()


class Common(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # yapf: disable
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.humanize',
        'django.contrib.sites',
        'whitenoise.runserver_nostatic',
        'django.contrib.staticfiles',
        'drf_api_logger',
        'rest_framework',
        'rest_framework.authtoken',
        'drf_yasg',
        'encrypted_fields',
        'backend.app',
    ]
    # yapf: enable

    # yapf: disable
    MIDDLEWARE = [
        'django.middleware.gzip.GZipMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'drf_api_logger.middleware.api_logger_middleware.APILoggerMiddleware',
    ]
    # yapf: enable

    ROOT_URLCONF = 'backend.urls'

    # yapf: disable
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
    # yapf: enable

    WSGI_APPLICATION = 'backend.wsgi.application'

    DATABASES = values.DatabaseURLValue('sqlite:///{}'.format(
        os.path.join(BASE_DIR, 'db.sqlite3')))

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    LANGUAGE_CODE = 'pt-br'
    TIME_ZONE = 'America/Sao_Paulo'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = False

    # Project Settings
    SITE_ID = 1
    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    DRF_API_LOGGER_DATABASE = True

    FIELD_ENCRYPTION_KEYS = [os.environ.get('FIELD_ENCRYPTION_KEY')]

    REST_FRAMEWORK = {
        'DEFAULT_SCHEMA_CLASS':
        'rest_framework.schemas.coreapi.AutoSchema',
        'DEFAULT_AUTHENTICATION_CLASSES':
        ('rest_framework_simplejwt.authentication.JWTAuthentication', ),
        'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer'],
        'TEST_REQUEST_DEFAULT_FORMAT':
        'json',
    }

    SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    }

    DATE_INPUT_FORMATS = '%Y-%m-%d'
    DATETIME_INPUT_FORMATS = '%Y-%m-%dT%H:%M'
    TIME_FORMAT = 'H:M'
    TIME_INPUT_FORMATS = [
        '%H:%M',
        '%H:%M:%S',
    ]

    SWAGGER_SETTINGS = {
        "SUPPORTED_SUBMIT_METHOD": [
            'get',
            'post',
            'put',
            'delete',
        ],
        'USE_SESSION_AUTH': False,
        "LOGIN_URL": "/",
        "LOGOUT_URL": "/",
        'SECURITY_DEFINITIONS': {
            'api_key': {
                'type': 'apiKey',
                'description': 'Personal API Key Authorization',
                'name': 'Token',
                'in': 'header',
            }
        },
        'APIS_SORTER': 'alpha',
        "TAGS_SORTER": 'alpha',
        "SHOW_REQUEST_HEADERS": True,
        "VALIDATOR_URL": None  # An API key
    }


class Development(Common):
    """
    The in-development settings and the default configuration.
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DEBUG = os.environ.get('DEBUG')
    ALLOWED_HOSTS = ['*']
    INTERNAL_IPS = ['127.0.0.1']
    CORS_ALLOW_ALL_ORIGINS = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')


class Staging(Common):
    """
    The in-staging settings and the default configuration.
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DEBUG = False
    ALLOWED_HOSTS = ['*']
    INTERNAL_IPS = ['127.0.0.1']
    CORS_ALLOW_ALL_ORIGINS = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_SECURE = False
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles/')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')


class Production(Common):
    """
    The in-production settings and the default configuration.
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DEBUG = False
    ALLOWED_HOSTS = ['*']
    INTERNAL_IPS = ['127.0.0.1']
    CORS_ALLOW_ALL_ORIGINS = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_SECURE = False
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles/')]
    MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles')
