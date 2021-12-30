from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from core.models import FablabBasePage

class AbstractArticlePage(FablabBasePage):
	image = models.ForeignKey(
		'core.FablabImage',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)

	date = models.DateField()

	introduction = models.CharField(max_length=255)

	body = RichTextField()

	content_panels = FablabBasePage.content_panels + [
		ImageChooserPanel("image"),
		FieldPanel("date"),
		FieldPanel("introduction"),
		FieldPanel("body"),
	]

	class Meta:
		abstract=True