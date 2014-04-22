# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

SECRET_KEY = '{{ secret_key }}'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'gunicorn',
    'south',
    'django_gears',
    'imagekit',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_L10N = True
USE_TZ = False

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public', 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

FILE_UPLOAD_MAX_MEMORY_SIZE = int(10 * 1024 * 1024)


GEARS_ROOT = os.path.join(BASE_DIR, 'static')
GEARS_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

GEARS_PUBLIC_ASSETS = (
    'javascripts/application.js',
    'stylesheets/application.css',
)
GEARS_COMPILERS = {
    '.scss': 'gears_sass.SASSCompiler',
    '.coffee': 'gears_coffeescript.CoffeeScriptCompiler',
}
GEARS_COMPRESSORS = {
    'application/javascript': 'gears_uglifyjs.UglifyJSCompressor',
    'text/css': 'gears_clean_css.CleanCSSCompressor',
}

IMAGEKIT_CACHEFILE_DIR = 'cache'
