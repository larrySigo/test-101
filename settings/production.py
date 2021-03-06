import dj_database_url


DATABASES[‘default’] = dj_database_url.config()
DEBUG = False

ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = (‘HTTP_X_FORWARDED_PROTO’, ‘https’)

STATIC_URL = '/static/'
 STATICFILES_DIRS = ( os.path.join(BASE_DIR,'static'),
 )
 STATIC_ROOT = os.path.join(BASE_DIR,'static-cdn')