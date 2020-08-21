from .base import *
DEBUG = False
ALLOWED_HOSTS = ['ip-address','www.your-website.com']


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'e-commerse',
        'USER':'root',
        'PASSWORD':'Momdad@143',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}

STRIPE_PUBLIC_KEY = 'your-live-public-key'
STRIPE_SECRET_KEY = 'your-live-secret-key'