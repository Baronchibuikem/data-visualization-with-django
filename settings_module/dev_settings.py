from settings_module.base_settings import *


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "wordcloud",
        "USER": "postgres",
        # "PASSWORD": "postgres",
        "PASSWORD": "12345",
        # "HOST": "wordcloud",
        "HOST": "localhost",
        "PORT": 5432,
    }
}
