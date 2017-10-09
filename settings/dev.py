from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Disqus
DISQUS_WEBSITE_SHORTNAME = 'icehockeysite'

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_jdJD1T7I9smh6Qem2d7eJIXP')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_vfYulusugV6nOunj56tb5ELk')
