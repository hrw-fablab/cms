from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from abstract.pages.flex import AbstractFlexPage

from ..blocks import FlexBlock

class QuFlexPage(AbstractFlexPage):
	template = "pages/flex.html"

	parent_page_types = ["QuHomepage"]
	subpage_type = []

	body = StreamField(FlexBlock())

	content_panels = Page.content_panels + [
		StreamFieldPanel("body"),
	]

	class Meta:
		verbose_name = "QuFablab Flexseite"