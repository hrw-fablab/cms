from .base import *

DEBUG = True

SECRET_KEY = str(os.environ.get("SECRET_KEY"))

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")

print(ALLOWED_HOSTS)

try:
    from .local import *
except ImportError:
    pass
