from django.db import models
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class Footer(BaseSetting):
	street = models.CharField(max_length=255)
	housenumber = models.CharField(max_length=20)
	place = models.CharField(max_length=255)
	plz = models.CharField(max_length=255)
	email = models.CharField(max_length=255)

	contact = models.ForeignKey(
		'wagtailcore.Page', 
		null=True,
		blank=True,
		on_delete=models.SET_NULL, 
		related_name='+')
	
	impressum = models.ForeignKey(
		'wagtailcore.Page', 
		null=True,
		blank=True,
		on_delete=models.SET_NULL, 
		related_name='+')

	data_protection = models.ForeignKey(
		'wagtailcore.Page', 
		null=True,
		blank=True,
		on_delete=models.SET_NULL, 
		related_name='+')
	
	facebook = models.URLField(null=True)
	instagram = models.URLField(null=True)
	youtube = models.URLField(null=True)
	thingiverse = models.URLField(null=True)
	twitter = models.URLField(null=True)

	panels = [
		MultiFieldPanel(
			[
			FieldPanel("street"),
			FieldPanel("housenumber"),
			FieldPanel("place"),
			FieldPanel("plz"),
			FieldPanel("email"),
			],heading="Adress"
		),
		MultiFieldPanel(
			[
			PageChooserPanel("contact"),
			PageChooserPanel("impressum"),
			PageChooserPanel("data_protection"),
			],heading="Service"
		),
		MultiFieldPanel(
			[
			FieldPanel("facebook"),
			FieldPanel("instagram"),
			FieldPanel("youtube"),
			FieldPanel("thingiverse"),
			FieldPanel("twitter"),
			],heading="Social Media"
		),
	]