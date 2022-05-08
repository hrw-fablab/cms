from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "DevelopmentKeyReplaceInProduction"

SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]
