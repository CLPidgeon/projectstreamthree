from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Disqus
DISQUS_WEBSITE_SHORTNAME = 'icehockeysite'

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_jdJD1T7I9smh6Qem2d7eJIXP')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_vfYulusugV6nOunj56tb5ELk')

SITE_URL = 'https://ice-hockey-site.herokuapp.com'
ALLOWED_HOSTS.append('ice-hockey-site.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}