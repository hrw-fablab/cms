from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from abstract.pages.home import AbstractHomePage
from abstract.pages.folder import AbstractFolderPage
from .blocks import StructBlock

class HomePage(AbstractHomePage):
	template = "pages/home.html"

	body = StreamField(StructBlock())

	content_panels = Page.content_panels + [
		StreamFieldPanel("body"),
	]

class FolderPage(AbstractFolderPage):
	parent_page_types = ["Homepage"]
	subpage_type = []
