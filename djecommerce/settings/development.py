from .base import *
from decouple import config

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Add dev-only apps
INSTALLED_APPS += [
    'debug_toolbar',
]

# Add dev-only middleware
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# ✅ Required by django-allauth >= 0.61.0
# (Already added in base.py, but double-check it's there)
if 'allauth.account.middleware.AccountMiddleware' not in MIDDLEWARE:
    MIDDLEWARE.insert(
        MIDDLEWARE.index('django.contrib.auth.middleware.AuthenticationMiddleware') + 1,
        'allauth.account.middleware.AccountMiddleware'
    )

# Django Debug Toolbar config
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

# SQLite Dev Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe Test Keys from .env
STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY', default='')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY', default='')
