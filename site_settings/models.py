from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMedia(BaseSetting):
	facebook = models.URLField()
	instagram = models.URLField()
	youtube = models.URLField()
	thingiverse = models.URLField()
	twitter = models.URLField()