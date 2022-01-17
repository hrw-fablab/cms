from wagtail.core.models import Page, Site
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from abstract.pages.home import AbstractHomePage
from ..blocks import HomeBlock


class HomePage(AbstractHomePage):
    template = "pages/home.html"

    body = StreamField(HomeBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Fablab Startseite"
