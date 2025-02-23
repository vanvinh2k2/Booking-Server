"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gm===#j9k*ko@riu(kf=2hc)g9h(i2)c^yy)=xq_m9f-6_f$%b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'daphne',
    'django.contrib.staticfiles',
    'core',
    'auths',
    'chatterbot',
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
    'rest_framework_simplejwt',
    # 'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
]

MIDDLEWARE = [
    # 'channels.middleware.AuthenticationMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'core.default.default',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

CORS_ALLOWED_ORIGINS = ['*']

# CORS_ORIGIN_ALLOW_ALL = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'restaurant_booking',
        'USER' : 'root',
        'PASSWORD' : '',
        'HOST' : 'localhost' 
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "mssql",
#         "NAME": "new4",
#         "HOST": "LAPTOP-AMQ9ETT3\SQLEXPRESS",
#         "PORT": "",
#         "OPTIONS": {
#             "driver": "ODBC Driver 17 for SQL Server",
#             'Trusted_Connection': 'Yes', 
#         },
#     },
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'Capstone_1',
#         'ENFORCE_SCHEMA': True,
#         'CLIENT': {
#             'host': 'mongodb+srv://ngov6769:2432002@cluster0.sv10xw9.mongodb.net/?retryWrites=true&w=majority',
#             'port': 27017,
#             'username': 'ngov6769',
#             'password': '2432002',
#             'authSource': 'admin',
#             'authMechanism': 'SCRAM-SHA-1',
#         }
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

ASGI_APPLICATION = 'app.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            'hosts': [('127.0.0.1', 6379)]
        }
    },
}



MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTH_USER_MODEL = 'auths.User'

REST_FRAMEWORK_SIMPLEJWT = {
    'USER_ID_FIELD': 'uid',
}
CKEDITOR_UPLOAD_PATH = 'uploads/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_header": "Restaurant Reservation",
    "site_brand": "Restaurant Reservation",
    "site_logo": "img/logo1.png",
    "copyright": "Team_C1SE.37@gmail.com",

    "icons": {
        "auths.ContactUs": "far fa-address-book",
        "auth.Group": "fas fa-users",
        "auths.User": "fas fa-user",
        "core.Address": "fas fa-map-marker-alt",
        "core.ChatMessage": "far fa-comment-dots",
        "core.Category": "fab fa-canadian-maple-leaf",
        "core.Restaurant": "fas fa-utensils",
        "core.Order": "fab fa-first-order",
        "core.OrderItem": "fas fa-tasks",
        "core.RestaurantReview": "fas fa-comments",
        "core.Dish": "fas fa-hamburger",
        "core.Wishlist": "fas fa-thumbs-up",
        "core.Table": "fas fa-chair",
    },
}

CKEDITOR_CONFIGS = {
    'default': {
        'skin': "moono",
        'codeSnippet_theme': 'monokai',
        'toolbar': 'all',
        'height': 300,
        'width': 600,
        'extraPlugins': ','.join(
            [
                'codesnippet',
                'widget',
                'dialog'
            ]
        )
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ngov6769@gmail.com'
EMAIL_HOST_PASSWORD = 'jnnaabzpmliwlvqe'