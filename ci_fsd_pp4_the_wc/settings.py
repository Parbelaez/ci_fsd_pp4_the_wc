from pathlib import Path
import os
import dj_database_url
from django.contrib.messages import constants as messages

if os.path.isfile("env.py"):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# To clearly indicate that the templates folder is inside the project folder
# this way, allauth will be able to find the templates folder as well.
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# For summernote
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEBUG' in os.environ

# X_FRAME_OPTIONS = 'SAMEORIGIN'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.herokuapp.com'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'django_summernote',
    'crispy_forms',
    'cloudinary',
    # Since version 2, the styling is a separate package.
    # https://django-crispy-forms.readthedocs.io/en/latest/install.html
    # Remember to add the template pack to the settings.py file.
    # and pip3 install crispy-bootstrap4
    'crispy_bootstrap4',
    'thewcwebpage',
    # The position should be after the app making use of it.
    # unless, the custom templates will not work.
    'allauth',  # allauth added for thewcwebpage app
    'allauth.account',  # allauth added for thewcwebpage app
    'allauth.socialaccount',  # allauth added for thewcwebpage app
]

# We need to tell Django the site number that we will apply this to.
# This is useful when we have more than one site running on the same
# Django instance.
SITE_ID = 1

# This is the URL that the user will be redirected to after logging in.
LOGIN_REDIRECT_URL = '/'
# This is the URL that the user will be redirected to after logging out.
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_FORMS = {'signup': 'thewcwebpage.forms.CustomSignupForm'}

# This is the mapping of the message level (e.g. messages.ERROR) to a CSS class.
# https://docs.djangoproject.com/en/4.2/ref/contrib/messages/#message-tags
# As bootstrap will be used, we need to use the bootstrap alert classes.
# https://getbootstrap.com/docs/5.0/components/alerts/

MESSAGE_TAGS = {
    messages.ERROR: 'alert-danger',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.INFO: 'alert-info',
    messages.DEBUG: 'alert-secondary',
}

# Crispy Forms does not support Bootstrap 5 yet, so we need to set the
# template pack to Bootstrap 4.
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'ci_fsd_pp4_the_wc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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



WSGI_APPLICATION = 'ci_fsd_pp4_the_wc.wsgi.application'

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "https://*.gitpod.io",
    "https://*.herokuapp.com",
]

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# This will avoid the need for an SMTP server as e-mails will be printed
# to the console. (This is useful for testing purposes.)
# https://stackoverflow.com/questions/21563227/django-allauth-example-errno-61-connection-refused
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_VERIFICATION = 'none'

print("DEBUG is", DEBUG)