from django.db import models
from wagtail.admin.edit_handlers import (
	FieldPanel,
	FieldRowPanel,
	MultiFieldPanel,
)
from wagtail.core.models import TranslatableMixin
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

class Author(models.Model):
	first_name = models.CharField("First name", max_length=254, blank=False)
	last_name = models.CharField("Last name", max_length=254, blank=False)
	
	image = models.ForeignKey(
		'core.FablabImage',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)

	panels = [
		MultiFieldPanel([
			FieldRowPanel([
				FieldPanel('first_name'),
				FieldPanel('last_name'),
			])
		], "Name"),
		ImageChooserPanel('image')
	]

	def __str__(self):
		return self.last_name

	class Meta:
		verbose_name = "Autor"
		verbose_name_plural = "Autoren"


class DeviceCategory(TranslatableMixin):
	name = models.CharField("Category Name", max_length=255, blank=False)
	
	panels = [
		FieldPanel('name'),
	]

	def __str__(self):
		return self.name


class ProjectCategory(TranslatableMixin):
	name = models.CharField("Category Name", max_length=255, blank=False)
	
	panels = [
		FieldPanel('name'),
	]

	def __str__(self):
		return self.name


class Tag(TranslatableMixin):
	name = models.CharField("Tag Name", max_length=255, blank=False)

	panels = [
		FieldPanel('name'),
	]

	def __str__(self):
		return self.name

register_snippet(Tag)
register_snippet(Author)
register_snippet(DeviceCategory)
register_snippet(ProjectCategory)