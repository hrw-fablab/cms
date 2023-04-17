from .base import *  # noqa

DEBUG = False

SECRET_KEY = str(os.environ.get("SECRET_KEY"))  # noqa

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_NAME"),  # noqa
        "USER": os.environ.get("DB_USER"),  # noqa
        "PASSWORD": os.environ.get("DB_PASSWORD"),  # noqa
        "HOST": os.environ.get("DB_HOST"),  # noqa
        "PORT": os.environ.get("DB_PORT"),  # noqa
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}
