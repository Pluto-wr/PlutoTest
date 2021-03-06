"""
Django settings for PlutoTest project.

Generated by 'django-admin startproject' using Django 2.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9lh!*u7=@grrxvd7z0_82cb@jq$4j_i4b#bu3zgjmw9g=(=3h)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition
# APP列表（应用）
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 注册子应用，子应用名.apps.ProjectsConfig
    'rest_framework',
    'django_filters',
    'drf_yasg',
    # 'corsheaders' # 解决跨域

    'projects.apps.ProjectsConfig',
    'interfaces.apps.InterfacesConfig',
    'user.apps.UesrConfig',
]

# DRF相关配置
REST_FRAMEWORK = {
    # 默认响应渲染类
    'DEFAULT_RENDERER_CLASSES': (
        # json渲染类为第一优先级
        'rest_framework.renderers.JSONRenderer',
        # 可浏览的API渲染为第二优先级
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    # 设置全局默认排序、过滤引擎
    'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.OrderingFilter',
                                'django_filters.rest_framework.backends.DjangoFilterBackend'],
    # 在全局指定分页的引擎
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 指定定制的分页引擎，因已经重写PAGE_SIZE。所以这里可以不用指定
    'DEFAULT_PAGINATION_CLASS': 'utils.pagination.PageNumberPaginationManual',
    # 同时必须指定每页显示的条数
    # 'PAGE_SIZE': 3,

    # coreapi自动生成api文档
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

    # 全局权限类
    # 'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated', ],

    # 认证类
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # 指定使用jwt_Token认证
        'rest_framework.authentication.SessionAuthentication',   # session会话认证
        'rest_framework.authentication.BasicAuthentication'  # Basic类型的认证,(账号和密码)
    ],
}

# jwt认证相关配置
JWT_AUTH = {
    # jwt token默认5min过期,这边更改为过期时间为1天
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    # 更改Token前缀为P P token
    'JWT_AUTH_HEADER_PREFIX': 'P',
    # 更改登录成功返回的内容
    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'utils.jwt_handler.jwt_response_payload_handler',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 跨域中间件
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 添加白名单
# CORS_ORIGIN_ALLOW_ALL为True,指定所有域名都可以访问后端接口,默认为False
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST指定能够访问后端接口的ip域名列表
# CORS_ORIGIN_WHITELIST = [
#
# ]

# 允许跨域时携带Cookie,默认为False
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'PlutoTest.urls'

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

WSGI_APPLICATION = 'PlutoTest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# MySql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_django',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# 解决drf-yasg报错
SWAGGER_SETTINGS = {
    "DEFAULT_GENERATOR_CLASS": "rest_framework.schemas.generators.BaseSchemaGenerator",
}


# # 设置日志
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s -- %(asctime)s - %(name)s - %(message)s'
        },
        'simple': {
            # 'format': '%(levelname)s -- %(asctime)s - %(name)s - %(message)s'
            'format': '%(asctime)s - [%(levelname)] - %(name)s -[msg]%(message)s - [%(filename)s:%(lineno)d ]'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志，日志会以文件的方式保存到项目目录下的 logs 文件夹下面；
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/PlutoTest.log'),  # 日志文件的位置
            'maxBytes': 100 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'simple',
            'encoding': 'utf-8'
        },
    },
    'loggers': {  # 日志器
        'PlutoTest': {  # 定义了一个名为PlutoTest的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'DEBUG',  # 日志器接收的最低日志级别为 DEBUG
        },
    }
}

# import os
# import os.path, time, datetime
#
# logdir = "/data0/www/applogs"
#
# for parent, dirnames, filenames in os.walk(logdir):
#     for filename in filenames:
#         fullname = parent + "/" + filename  # 文件全称
#         createTime = int(os.path.getctime(fullname))  # 文件创建时间
#         nDayAgo = (datetime.datetime.now() - datetime.timedelta(days=2))  # 当前时间的n天前的时间
#         timeStamp = int(time.mktime(nDayAgo.timetuple()))
#         if createTime < timeStamp:  # 创建时间在n天前的文件删除
#             os.remove(os.path.join(parent, filename))