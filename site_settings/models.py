from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMedia(BaseSetting):
	facebook = models.URLField()
	instagram = models.URLField()
	youtube = models.URLField()
	thingiverse = models.URLField()
	twitter = models.URLField()

@register_setting
class Adress(BaseSetting):
	street = models.CharField(max_length=255)
	housenumber = models.CharField(max_length=20)
	place = models.CharField(max_length=255)
	plz = models.CharField(max_length=255)
	email = models.CharField(max_length=255)