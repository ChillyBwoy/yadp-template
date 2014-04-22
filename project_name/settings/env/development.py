# -*- coding: utf-8 -*-

import os
import sys

from {{ project_name }}.settings.base import *

TEST = 'test' in sys.argv
DEBUG = True
TEMPLATE_DEBUG = DEBUG
GEARS_DEBUG = DEBUG

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

INTERNAL_IPS = (
    '127.0.0.1',
)

if not TEST:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db/development.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME':  ':memory',
        },
    }

INSTALLED_APPS += (
    'debug_toolbar',
)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
