"""
Django settings for wecare project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

import datetime #56에서 시작되는 JWT_AUTH 의 토큰 유효기간을 설정하기 위한 datetime import
import os  #image가 추가 될때 경로

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v@%qp(h)v*-7p^fv*3^6#lkgqoz+9p^&&41h05xi#b^58r-+!^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []

#JWT 와 REact를 위한 연결

CORS_ORIGIN_WHITELIST = ['http://localhost:3000'] #아까 설치한 corsheaders로 해당 서버와 연결할 서버의 url을 작성해준모습


REST_FRAMEWORK = { # 추가
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  #인증된 회원만 액세스 허용
        'rest_framework.permissions.AllowAny',         #모든 회원 액세스 허용
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': ( #api가 실행됬을 때 인증할 클래스를 정의해주는데 우리는 JWT를 쓰기로 했으니
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication', #이와 같이 추가해준 모습이다.
    ),
}

JWT_AUTH = { # 추가
   'JWT_SECRET_KEY': SECRET_KEY,
   'JWT_ALGORITHM': 'HS256',
   'JWT_VERIFY_EXPIRATION' : True, #토큰검증
   'JWT_ALLOW_REFRESH': True, #유효기간이 지나면 새로운 토큰반환의 refresh
   'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=30),  # Access Token의 만료 시간
   'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=3), # Refresh Token의 만료 시간
   'JWT_RESPONSE_PAYLOAD_HANDLER': 'wecare.custom_responses.my_jwt_response_handler'
}



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'rest_framework',

    'family',
    'user',
    'facility',
    'facility_admin',


    'rest_framework',  # 추가
    'rest_framework_jwt',  # 추가
    'corsheaders',  # 추가


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


    'corsheaders.middleware.CorsMiddleware',  # 추가

]

ROOT_URLCONF = 'wecare.urls'

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

WSGI_APPLICATION = 'wecare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'wecare',
#         'USER': 'remote',
#         'PASSWORD': '1234',
#         'HOST': '3.15.69.19',
#         'PORT': '3306',
#     }
# }


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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
