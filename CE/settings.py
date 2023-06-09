"""
Django settings for CE project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l!s2(muq32tbp5_-yt8-od2jst9fs(2j-^r$_=b)2#4+sw2r4)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    #'collabo_events',
    #'events_api',
    'modeltranslation',
    'simple_mail',
    #'ckeditor',

    'django.contrib.gis',
    #'jet.dashboard',
    #'jet',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'drf_accountkit',
    'rest_framework',
    'rest_framework.authtoken',
    'storages',
    'social_django',

    'crispy_forms',
    'oauth2_provider',
    
    'events_api',
    'collabo_events',
    'phonenumber_field',
    'qr_code',
    'tinymce',
    'filebrowser',
    'corsheaders',
    'cities_light',
    'places',
    'timezone_field',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.gzip.GZipMiddleware'
]

ROOT_URLCONF = 'CE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates') ],
        
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'CE.wsgi.application'


TINYMCE_DEFAULT_CONFIG = {
    'height': 200,
    'width': 900,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        # OAuth
        # 'oauth2_provider.ext.rest_framework.OAuth2Authentication',  # django-oauth-toolkit < 1.0.0
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
    ),
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.ModelSerializer',
    'DEFAULT_PERMISSION_CLASSES':
        ('rest_framework.permissions.IsAdminUser',),

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),

    'DATETIME_FORMAT': "%Y-%m-%dT%H:%M:%S.%fZ",
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
    ),
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'PAGE_SIZE': 9,

    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',



    #'EXCEPTION_HANDLER':'SainaPro.vdocipher.utils.custom_exception_handler'



}


AUTHENTICATION_BACKENDS = (

    # Others auth providers (e.g. Google, OpenId, etc)
    'social_core.backends.google.GoogleOAuth2',
    #'social_core.backends.google.GoogleAppOAuth2',

    #'social_core.backends.google.GoogleOpenId',
    #'social_core.backends.google.GoogleOAuth'

    # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social.backends.email.EmailAuth',

    # django-rest-framework-social-oauth2
    'rest_framework_social_oauth2.backends.DjangoOAuth2',

    # Django
    'django.contrib.auth.backends.ModelBackend',

)




# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        # PostgreSQL database
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'SampleDB',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',

       
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


# Custom Django auth settings

AUTH_USER_MODEL = 'collabo_events.User'

LOGIN_URL = 'login'

LOGOUT_URL = 'logout'

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'


# Messages built-in framework






CITIES_LIGHT_TRANSLATION_LANGUAGES = ['fr', 'en']
CITIES_LIGHT_INCLUDE_COUNTRIES = ['FR']
CITIES_LIGHT_INCLUDE_CITY_TYPES = ['PPL', 'PPLA', 'PPLA2', 'PPLA3', 'PPLA4', 'PPLC', 'PPLF', 'PPLG', 'PPLL', 'PPLR', 'PPLS', 'STLMT',]


# Third party apps configuration

CRISPY_TEMPLATE_PACK = 'bootstrap4'


GOOGLE_MAPS_API_KEY = 'AIzaSyAsvMlJvtUMZvEV_Xe69QnECUpShXbxnKc'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')




SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

DRFSO2_PROPRIETARY_BACKEND_NAME ='django'

SOCIAL_AUTH_FACEBOOK_KEY ='513389439090636'


SOCIAL_AUTH_FACEBOOK_SECRET= '5da1bf52c8302f68afd448d5256ddb4f'

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from facebook. Email is not sent by default, to get it, you must request the email permission:
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email','user_likes']

#FACEBOOK_EXTENDED_PERMISSIONS = ['email']
SOCIAL_AUTH_FACEBOOK_API_VERSION = '3.0'

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'locale': 'pl_PL',
    'fields': 'id, name, email,gender,hometown,birthday,address'
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '428065779114-n5161ru1ba7iukbuhbtmu7cdpj6q9p5d.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ='DZLRvvwKz66pOBDIUynPEkj2'


#send email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'collabozartek@gmail.com'
EMAIL_HOST_PASSWORD = 'collabo@zartek123'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


SIMPLE_MAIL_USE_CKEDITOR = True
SIMPLE_MAIL_USE_MODELTRANSALTION = True

SECURITY_EMAIL_SENDER = 'collabozartek@gmail.com'
# enable django-modeltranslation integration
SIMPLE_MAIL_USE_MODELTRANSALTION = False
# enable django-ckeditor integration
SIMPLE_MAIL_USE_CKEDITOR = False
# set default email template
#SIMPLE_MAIL_DEFAULT_TEMPLATE = 'simple_mail/default.html'
# enable/disable cssutils warning logs
SIMPLE_MAIL_LOG_CSS_WARNING = False


# SMS configuration

SENDSMS_BACKEND = 'myapp.mysmsbackend.SmsBackend'


SNS_CERT_DOMAIN_REGEX = r"sns.[a-z0-9\-]+.amazonaws.com$" # Regex to match on cert domain
SNS_VERIFY_CERTIFICATE = True # Whether to verify signature against certificate




AWS_ACCESS_KEY_ID_SAL = 'AKIAJX7MQLBOPMRNKC6A',
AWS_SECRET_ACCESS_KEY_SAL = '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',
REGION_NAME = 'ap-southeast-1',
#CKEDITOR_BASEPATH="/static/ckeditor/ckeditor"

DATA_UPLOAD_MAX_NUMBER_FIELDS=10240


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'qr-code': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'qr-code-cache',
        'TIMEOUT': 3600
    }
}

QR_CODE_CACHE_ALIAS = 'qr-code'
QR_CODE_URL_PROTECTION = {
    'TOKEN_LENGTH': 30,                         # Optional random token length for URL protection. Defaults to 20.
    'SIGNING_KEY': 'my-secret-signing-key',     # Optional signing key for URL token. Uses SECRET_KEY if not defined.
    'SIGNING_SALT': 'my-signing-salt',          # Optional signing salt for URL token.
    'ALLOWS_EXTERNAL_REQUESTS_FOR_REGISTERED_USER': True  # Tells whether a registered user can request the QR code URLs from outside a site that uses this app. It can be a boolean value used for any user or a callable that takes a user as parameter. Defaults to False (nobody can access the URL without the security token).
}

#BOOKING_TIME_INTERVAL = 'day'


PLACES_MAPS_API_KEY='AIzaSyBeB4MqhaqWaQShi3WRPfpJJKKzzrWRjUs'
PLACES_MAP_WIDGET_HEIGHT=480
PLACES_MAP_OPTIONS='{"center": { "lat": -34.397, "lng": 150.644 }, "zoom": 10}'
PLACES_MARKER_OPTIONS='{"draggable": true}'

FACEBOOK_APP_ID = "333260200721985"
ACCOUNT_KIT_APP_SECRET = "7626acd5c8ff3cf74de462d51ca32e7d"
#c368b25aa042bebf157384c162fa70cc

ACCOUNT_KIT_VERSION = "v1.0"
FILEBROWSER_DIRECTORY = ''
DIRECTORY = ''

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://localhost:8080',
]



MEDIA_URL = '/media/'
#STATIC_URL = '/static/'

#STATICFILES_DIRS= [
    #os.path.join(BASE_DIR , "static/")
#]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_cdn")
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"media_cdn")


AWS_ACCESS_KEY_ID = 'AKIASOA2CBB4SDQEBNUA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'getcollabo-assetsserver'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION_MEDIA = 'media'

AWS_LOCATION = 'static'
AWS_MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION_MEDIA)


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'CE.storage_backends.MediaStorage'  # <-- here is where we reference it




PAYFORT_ACCESS_CODE ="QvMQiaL3flsiTGSu7FMe"
PAYFORT_MERCHANT_IDENTIFIER ='AstdpYTL'
PAYFORT_LANGUAGE ='en'
PAYFORT_CURRENCY ='SAR'
PAYFORT_URL ='https://sbpaymentservices.payfort.com/FortAPI/paymentApi'


CRISPY_TEMPLATE_PACK = 'bootstrap4'

