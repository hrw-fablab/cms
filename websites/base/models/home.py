from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from abstract.pages.home import AbstractHomePage
from ..blocks import HomeBlock


class HomePage(AbstractHomePage):
    template = "pages/home.html"

    body = StreamField(HomeBlock(), blank=True)

    content_panels = AbstractHomePage.content_panels + [
        StreamFieldPanel("body"),
    ]