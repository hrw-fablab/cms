from django.db import models

from wagtail.core.models import Page, Site
from wagtail.documents.models import Document, AbstractDocument
from wagtail.images.models import Image, AbstractImage, AbstractRendition

class FablabImage(AbstractImage):
	credit = models.CharField(max_length=255, blank=True)

	admin_form_fields = Image.admin_form_fields + ('credit',)

class FablabRendition(AbstractRendition):
	image = models.ForeignKey(
		"FablabImage", on_delete=models.CASCADE, related_name='renditions'
	)

	class Meta:
		unique_together = (('image', 'filter_spec', 'focal_point_key'),)

class FablabDocument(AbstractDocument):
	credit = models.CharField(max_length=255, blank=True)

	admin_form_fields = Document.admin_form_fields + ('credit',)

class FablabBasePage(Page):
	def get_context(self, request):
		context = super().get_context(request)
		context['menuitems'] = Site.find_for_request(request).root_page.get_children().live().in_menu()
		return context

	class Meta:
		abstract=True