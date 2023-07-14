"""
Django settings for starprj project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=+&yzt_7^@4&^5b5o0%x^^3r%ohvth*%r)774aw^aqqfs^re2x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'user',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    'star_ratings',
    'test1',
    'test2',
    'test3',
    'test4',
    'test5',
    'test6',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mapstar.apps.MapstarConfig',
]

# 로그인
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
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

ROOT_URLCONF = 'starprj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],     # 이거 수정하면 오류가 나오.. html 파일 인식을 못합니다. 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 'django.core.context_processors.request', # TEMPLATE_CONTEXT_PROCESSORS 하위에 적으면 된다고 하는데, 그게 없어서 대신 여기에.
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'starprj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 미디어
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'user.User'

# static 파일
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

SOCIALACCOUNT_LOGIN_ON_GET = True # 카카오 로그인 기본 템플릿 없이 바로 이동
LOGIN_REDIRECT_URL = '/world' # 로그인 후 world 템플릿으로 이동
LOGOUT_REDIRECT_URL = '/' # 로그아웃 후 메인으로 이동
#LOGIN_URL = '/main' # 로그인 경로


# 카카오 로그인
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_REDIRECT_URL = '/world'
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'


# 바로 카카오 로그인 페이지로 넘어가도록
SOCIALACCOUNT_LOGIN_ON_GET = True

# 로그아웃 완료 후 이동할 템플릿
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
# 로그아웃 요청 후 즉시 로그아웃 되도록 (확인 페이지 x)
ACCOUNT_LOGOUT_ON_GET = True
# 미디어
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'user.User'

# static 파일
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

SOCIALACCOUNT_LOGIN_ON_GET = True # 카카오 로그인 기본 템플릿 없이 바로 이동
LOGIN_REDIRECT_URL = '/world' # 로그인 후 world 템플릿으로 이동
LOGOUT_REDIRECT_URL = '/' # 로그아웃 후 메인으로 이동
#LOGIN_URL = '/main' # 로그인 경로


# 카카오 로그인
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_REDIRECT_URL = '/world'
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'


# 바로 카카오 로그인 페이지로 넘어가도록
SOCIALACCOUNT_LOGIN_ON_GET = True

# 로그아웃 완료 후 이동할 템플릿
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
# 로그아웃 요청 후 즉시 로그아웃 되도록 (확인 페이지 x)
ACCOUNT_LOGOUT_ON_GET = True

# 카카오 로그인 필수 기능 변경
#ACCOUNT_AUTHENTICATION_METHOD = 'email'
#ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_UNIQUE_EMAIL = True
#ACCOUNT_USERNAME_REQUIRED = False
#ACCOUNT_USER_MODEL_USERNAME_FILED = None
# SITE_ID = 2   
SITE_ID = 2     # 카카오로그인 위해서 

# 템플릿
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'