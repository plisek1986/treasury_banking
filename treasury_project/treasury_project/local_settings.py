# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'treasury_banking',
        'HOST': 'localhost',
        'PASSWORD': 'krasnojarski2',
        'USER': 'postgres',
        'PORT': 5432
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6hrtv_#+z2o3*b!s-lirr4zni%f+s-u9(6$7i*%a=3fjnvlsv-'
