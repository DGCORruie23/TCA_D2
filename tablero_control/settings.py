from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='django-insecure-v1!($nd@2=4ye0j%ko65$^w=o6*3trmobv7m9mygzr+jb=it=c')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=1))

# GS_PROJECT_ID = 'tca-dgcor-2024'
# GS_BUCKET_NAME = 'django_tca_bucket'
# # GS_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', default='')
# STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"

# from google.oauth2 import service_account

# GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#     "./credentials.json"
# )


DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default='localhost 172.22.13.148').split(" ")

CSRF_TRUSTED_ORIGINS = os.environ.get("DJANGO_TRUSTED_ORIGINS", default='http://localhost http://172.22.13.148').split(" ")

LOGIN_REDIRECT_URL = '/dashboard/'
LOGIN_URL = 'log-in'
LOGOUT_REDIRECT_URL = 'index'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'usuarios',
    'dashboard',
    'tailwind',
    'estadistica',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tablero_control.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'tablero_control.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        "ENGINE": os.environ.get("SQL_ENGINE", 'django.db.backends.sqlite3'),
        "NAME": os.environ.get("MYSQL_DATABASE", os.path.join(os.path.join(BASE_DIR, "data"), "db.sqlite3")),
        "USER": 'root',
        "PASSWORD": 'rui23dgcor@',
        "HOST": 'db',
        "PORT": '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Archivos estáticos
BASE_DIR_ROOT = os.environ.get('BASE_DIR_ROOT', default=BASE_DIR)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR_ROOT, os.path.join("data", "static"))
# STATICFILES_DIRS = [os.path.join(BASE_DIR_ROOT, 'static')]

# Archivos de medios
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR_ROOT,'media')

SESSION_COOKIE_AGE = 360

DATA_UPLOAD_MAX_MEMORY_SIZE = None  # Removes the size limit
FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600  # Sets the limit to 100MB, for example

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Archivos de medios
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR_ROOT, os.path.join("data", "media"))
# MEDIA_URL = 'https://storage.googleapis.com/{}/media'.format(GS_BUCKET_NAME)
# MEDIA_ROOT = "media/"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





# """
# Django settings for tablero_control project.

# Generated by 'django-admin startproject' using Django 5.0.4.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/5.0/ref/settings/
# """

# from pathlib import Path
# import os
# import io
# from urllib.parse import urlparse
# import environ
# from google.cloud import secretmanager

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# env = environ.Env(DEBUG=(bool, False))
# env_file = os.path.join(BASE_DIR, ".env")

# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY', default='django-insecure-v1!($nd@2=4ye0j%ko65$^w=o6*3trmobv7m9mygzr+jb=it=c')

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = int(os.environ.get("DEBUG", default=1))

# # STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
# DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# # ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default='localhost 172.22.13.148').split(" ")

# APPENGINE_URL = env("APPENGINE_URL", default=None)
# if APPENGINE_URL:
#     # Ensure a scheme is present in the URL before it's processed.
#     if not urlparse(APPENGINE_URL).scheme:
#         APPENGINE_URL = f"https://{APPENGINE_URL}"

#     ALLOWED_HOSTS = [urlparse(APPENGINE_URL).netloc]
#     CSRF_TRUSTED_ORIGINS = [APPENGINE_URL]
#     SECURE_SSL_REDIRECT = True
# else:
#     ALLOWED_HOSTS = ["*"]

    

# if os.path.isfile(env_file):
#     # Use a local secret file, if provided

#     env.read_env(env_file)

# elif os.environ.get("GOOGLE_CLOUD_PROJECT", None):
#     # Pull secrets from Secret Manager
#     project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

#     client = secretmanager.SecretManagerServiceClient()
#     settings_name = os.environ.get("SETTINGS_NAME", "django_settings")
#     name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
#     payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")

#     env.read_env(io.StringIO(payload))
# else:
#     raise Exception("No local .env or GOOGLE_CLOUD_PROJECT detected. No secrets found.")
# [END gaestd_py_django_secret_config]

# project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

# client = secretmanager.SecretManagerServiceClient()
# settings_name = os.environ.get("SETTINGS_NAME", "django_settings")
# name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
# payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")

# env.read_env(io.StringIO(payload))



# LOGIN_REDIRECT_URL = '/dashboard/'
# LOGIN_URL = 'log-in'
# LOGOUT_REDIRECT_URL = 'index'


# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',

#     'usuarios',
#     'dashboard',
#     'tailwind',
#     'estadistica',

# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'tablero_control.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'tablero_control.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# #======================================

# DATABASES = {"default": env.db()}

# # If the flag as been set, configure to use proxy
# if os.getenv("USE_CLOUD_SQL_AUTH_PROXY", None):
#     DATABASES["default"]["HOST"] = "127.0.0.1"
#     DATABASES["default"]["PORT"] = 5432

# # [END gaestd_py_django_database_config]

# # Use a in-memory sqlite3 database when testing in CI systems
# # TODO(glasnt) CHECK IF THIS IS REQUIRED because we're setting a val above
# if os.getenv("TRAMPOLINE_CI", None):
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#             "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#         }
#     }

# #=================================

# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.sqlite3',
# #         'NAME': BASE_DIR / 'db.sqlite3',
# #     }
# # }


# # Password validation
# # https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = 'es-es'

# TIME_ZONE = 'America/Mexico_City'

# USE_I18N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.0/howto/static-files/

# # Archivos estáticos
# BASE_DIR_ROOT = os.environ.get('BASE_DIR_ROOT', default=BASE_DIR)

# STATIC_ROOT = "static"
# STATIC_URL = "/static/"
# STATICFILES_DIRS = []

# # STATIC_URL = 'static/'
# # STATIC_ROOT = os.path.join(BASE_DIR_ROOT, "static")
# # # STATICFILES_DIRS = [os.path.join(BASE_DIR_ROOT, 'static')]


# MEDIA_ROOT = "media"
# MEDIA_URL = "/media/"

# # # Archivos de medios
# # MEDIA_URL = '/media/'
# # MEDIA_ROOT = os.path.join(BASE_DIR_ROOT,'media')

# SESSION_COOKIE_AGE = 360

# DATA_UPLOAD_MAX_MEMORY_SIZE = None  # Removes the size limit
# FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600  # Sets the limit to 100MB, for example

# # STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# # # Archivos de medios
# # MEDIA_URL = '/media/'
# # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
