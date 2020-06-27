#coding=utf-8
"""
Django settings for axf project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b^5hg3=8a!)t^*4o9m2w!c0%5_h2g=wh44k03sal8oiz!ninqo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'HomeApp',
    'MarketApp',
    'CartApp',
    'MineApp',
    'UserApp',
    'OrderApp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'axf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'axf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'axf1905',
        'USER': 'dhf',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# 静态资源路径
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

CACHES = {
        'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}

# 放置图片路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/upload')

# 邮箱配置
# #这一项是固定的
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# smtp服务的邮箱服务器 我用的是163
EMAIL_HOST = 'smtp.163.com'
# smtp服务固定的端口是25
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = '17855370071@163.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'dhf123456'

# # 发送邮件设置
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # SMTP地址
# EMAIL_HOST = 'smtp.qq.com'
# # SMTP端口
# EMAIL_PORT = 465
# # 自己的邮箱
# EMAIL_HOST_USER = '2551628690@qq.com'
# # 自己的邮箱授权码，非密码
# EMAIL_HOST_PASSWORD = 'xxxxxxxxxx'

# 字体的路径
FONT_PATH = os.path.join(BASE_DIR, 'static/fonts/ADOBEARABIC-BOLD.OTF')

# 支付宝接口配置
APP_PRIVATE_KEY_STRING = open(os.path.join(BASE_DIR,'alipay_config/app_rsa_private_key.pem'),'r').read()
ALIPAY_PUBLIC_KEY_STRING = open(os.path.join(BASE_DIR,'alipay_config/alipay_rsa_public_key.pem'),'r').read()

# debug_toolbar
# # INTERNAL_IPS=('127.0.0.1')