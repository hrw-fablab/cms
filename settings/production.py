from .base import *

DEBUG = False

SECRET_KEY = str(os.getenv("SECRET_KEY"))

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

try:
    from .local import *
except ImportError:
    pass
