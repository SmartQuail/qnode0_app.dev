"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__,os.pardir))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get('DEBUG'))=="1"

ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    filter(None, os.environ.get('ALLOWED_HOSTS', '').split(','),
    )
)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'modelcluster',
    #'streams',
    
    #'webapp_0',
    #'social_django',
    
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.settings',
    'wagtail.contrib.routable_page',
    #'wagtail.contrib.postgres_search',
    #'wagtail.search.backends.database'
    'wagtail.contrib.modeladmin',
    
    'taggit',
    'django_extensions',
    'wagtailmarkdown',
    'crispy_forms',
    'crispy_bootstrap5',
    #'captcha',
    'wagtailcaptcha',
    "wagtailmenus",
    'wagtailmetadata',
    'webpack_loader',
    'django_comments',
    #'custom_comments.apps.CustomCommentsConfig',
    'rosetta',
    'parler',
    #'bootstrap4',
    'localflavor',
    'widget_tweaks',
    
    #'core',
    'sorl.thumbnail',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    
]
LOGIN_REDIRECT_URL = 'wagtailadmin_home'
WAGTAILIMAGES_MAX_UPLOAD_SIZE = 30 * 1024 * 1024
WAGTAILIMAGES_MAX_IMAGE_PIXELS = 300000000 #300MP

WAGTAILIMAGES_FORMAT_CONVERSIONS = {
    'jpg': 'jpeg',
    'webp': 'webp',
}

#Email setups
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_PORT          =  587
EMAIL_HOST_USER     = 'smartquail.info@gmail.com'
EMAIL_HOST_PASSWORD = 'ms1719183830'
EMAIL_USE_TLS       = True
DEFAULT_FROM_EMAIL  = EMAIL_HOST_USER
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'


#SECURE_SSL_REDIRECT = bool(int(os.environ.get('SECURE_SSL_REDIRECT',0)))
#CSRF_COOKIE_SECURE = bool(int(os.environ.get('CSRF_COOKIE_SECURE',0)))

#Email setups
#EMAIL_HOST          = 'smtp.domain.com'
#EMAIL_PORT          =  587
#EMAIL_HOST_USER     = 'info@juansilvaphoto.com'
#EMAIL_HOST_PASSWORD = 'A1T2J3C4'
#EMAIL_USE_SSL       = True
#DEFAULT_FROM_EMAIL  = EMAIL_HOST_USER
#EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'

ROOT_URLCONF = 'qnode0_app.urls'
WAGTAIL_SITE_NAME = 'Smart Business Media'
SITE_ID = 1 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtailmenus.context_processors.wagtailmenus',
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'qnode0_app.wsgi.application'

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
    }
}


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DB_NAME = os.environ.get("POSTGRES_DB"),
DB_PASS = os.environ.get("POSTGRES_PASSWORD"),
DB_USER = os.environ.get("POSTGRES_USER"),
DB_HOST = os.environ.get("POSTGRES_HOST"),
DB_PORT = os.environ.get("POSTGRES_PORT")

DB_IS_AVAIL = all([
    DB_NAME,
    DB_PASS,
    DB_USER,
    DB_HOST,
    DB_PORT
])

POSTGRES_READY=str(os.environ.get('POSTGRES_READY'))=="1"



if DB_IS_AVAIL and POSTGRES_READY:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': DB_HOST,
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASS,
            'PORT': DB_PORT,
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


from django.utils.translation import gettext_lazy as _

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)

LANGUAGE_CODE = 'es'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'
#STATIC_URL ='static/'
#MEDIA_URL = '/media/'

MEDIA_ROOT = '/vol/web/media'
STATIC_ROOT = '/vol/web/static'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#STATIC_ROOT =  os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


