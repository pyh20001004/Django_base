"""
Django settings for bookmanager project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rrc&zela3mz4ky^$o9b%!5hxew*a#&4$3lpbncgmoo_87o*bvw'

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式
# 在我们开发的时候，我们需要看到更多的信息，所以要开启debug模式
# 当我们的程序上线之后，就改为False
DEBUG = True
# 允许以什么样的形式来访问我们的项目 默认是 127.0.0.1
# * 的意思是可以使用ip也可以使用127
ALLOWED_HOSTS = ['*']


# Application definition
# 注册/安装子应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'book',  # 方案一
    'book.apps.BookConfig',  # 方案一
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

ROOT_URLCONF = 'bookmanager.urls'

#模板配置相关
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #告知系统，我们的模板文件放在哪里
        # 'DIRS': [os.path.join(BASE_DIR,'templates')],
        'DIRS':[],
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

WSGI_APPLICATION = 'bookmanager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# sqlite3 关系型数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# 设置语言
LANGUAGE_CODE = 'zh-Hans'   #'en-us'
# 设置时区
TIME_ZONE = 'Asia/Shanghai'  #'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# STATICFILES_DIRS告诉django,首先到STATICFILES_DIRS(根目录的static)里面寻找静态文件,
# 其次再到各个app的static文件夹里面找(注意, django查找静态文件是惰性查找,查找到第一个,就停止查找了)
#告知系统 我们的图片在哪里
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]