from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from abstract.pages.flex import AbstractFlexPage

from fablab_web.blocks import FlexBlock

class FlexPage(AbstractFlexPage):
	template = "pages/flex.html"

	parent_page_types = ["Folderpage", "Homepage"]
	subpage_type = []

	body = StreamField(FlexBlock())

	content_panels = Page.content_panels + [
		StreamFieldPanel("body"),
	]