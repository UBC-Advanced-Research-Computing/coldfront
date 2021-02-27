from coldfront.config.settings import ENV, PROJECT_ROOT

#------------------------------------------------------------------------------
# Database settings
#------------------------------------------------------------------------------
# Set this using the COLDFRONT_DB_URL env variable. Defaults to sqlite. 
#
# Examples:
#
# MariaDB:
#  COLDFRONT_DB_URL=mysql://user:password@127.0.0.1:3306/database
#
# Postgresql:
#  COLDFRONT_DB_URL=psql://user:password@127.0.0.1:8458/database
#------------------------------------------------------------------------------
DATABASES = {
    'default': ENV.db_url(
        var='COLDFRONT_DB_URL',
        default='sqlite:///'+PROJECT_ROOT('coldfront.db')
    )
}


#------------------------------------------------------------------------------
# Custom Database settings
#------------------------------------------------------------------------------
# You can also override this manually in local_settings.py, for example:
#
# NOTE: For mysql you need to: pip install mysqlclient
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'coldfront',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '',
#     },
# }
#
# NOTE: For postgresql you need to: pip install psycopg2
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'coldfront',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     },
# }
