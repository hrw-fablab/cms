from .base import *

DEBUG = False

SECRET_KEY = str(os.environ.get("SECRET_KEY"))

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")
