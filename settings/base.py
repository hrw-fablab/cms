"""
Django settings for cms project.

Generated by 'django-admin startproject' using Django 3.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
	'user',
	'core',
	'site_settings',
	'snippets',
	'search',
	'websites.fablab',
	'websites.qu_fablab',

	'wagtail_link_block',
	'wagtailmedia',
	'wagtail_localize',
	'wagtail_localize.locales',

	'wagtail.contrib.settings',
	'wagtail.contrib.forms',
	'wagtail.contrib.redirects',
	'wagtail.embeds',
	'wagtail.sites',
	'wagtail.users',
	'wagtail.snippets',
	'wagtail.documents',
	'wagtail.images',
	'wagtail.search',
	'wagtail.admin',
	'wagtail.core',

	'modelcluster',
	'taggit',

	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'wagtailthemes',
]

MIDDLEWARE = [
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',

	'django.middleware.locale.LocaleMiddleware',
	'wagtail.contrib.redirects.middleware.RedirectMiddleware',
	'wagtailthemes.middleware.ThemeMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			os.path.join(PROJECT_DIR, 'templates'),
		],
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
			'loaders': [
				'wagtailthemes.loaders.ThemeLoader',
				'django.template.loaders.filesystem.Loader',
				'django.template.loaders.app_directories.Loader',
			]
		},
	},
]

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
	}
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'de'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

WAGTAIL_I18N_ENABLED = True

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
	("de", "German"),
	("en", "English"),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_FINDERS = [
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
	os.path.join(PROJECT_DIR, './static_source'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static_source/'

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

# Wagtail settings

WAGTAIL_SITE_NAME = "cms"

# Search
# https://docs.wagtail.io/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
	'default': {
		'BACKEND': 'wagtail.search.backends.database',
	}
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://example.com'

# Use Custom User Model
AUTH_USER_MODEL = 'user.FablabUser'

WAGTAILIMAGES_IMAGE_MODEL = "core.FablabImage"

WAGTAILDOCS_DOCUMENT_MODEL = "core.FablabDocument"

WAGTAILMEDIA = {
	"MEDIA_MODEL": "core.FablabMedia",
	"MEDIA_FORM_BASE": "",
	"AUDIO_EXTENSIONS": [],
	"VIDEO_EXTENSIONS": [],
}

# Wagtail themes
# https://github.com/moorinteractive/wagtail-themes

WAGTAIL_THEME_PATH = 'themes'
WAGTAIL_THEMES = [
	('fablab', 'Fablab site'),
	('personal', 'Personal site')
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"