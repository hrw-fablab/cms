from dateutil.relativedelta import relativedelta
from wagtail.models import Orderable
from django.db import models

from wagtail.admin.panels import (
    InlinePanel,
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.fields import StreamField

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from abstract.pages.home import AbstractHomePage
from abstract.pages.folder import AbstractFolderPage
from abstract.pages.flex import AbstractFlexPage
from abstract.pages.index import AbstractIndexPage
from abstract.pages.article import AbstractArticlePage
from abstract.pages.search import AbstractSearchPage
from abstract.pages.project import AbstractProjectPage
from abstract.pages.base import AbstractBasePage

from abstract.models.links import Link, ExpireLink, PageLink
from forms.models import FabLabCaptchaEmailForm
from wagtail.admin.panels import TabbedInterface, ObjectList

from websites.base.blocks import (
    HomeBlock,
    FlexBlock,
    ProjectBlock,
    FormBlock,
)

from devices.models import Device

from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField


class HomePage(AbstractHomePage):
    subpage_type = [
        "FolderPgae",
        "FlexPage",
        "IndexPage",
        "DeviceIndexPage",
        "ProjectIndexPage",
        "SearchPage",
        "CollectionPage",
        "FormPage",
    ]

    template = "pages/flex.html"
    body = StreamField(HomeBlock(), blank=True, use_json_field=True)

    content_panels = AbstractHomePage.content_panels + [
        FieldPanel("body"),
    ]


class FolderPage(AbstractFolderPage):
    parent_page_types = ["HomePage"]
    subpage_type = ["FlexPage", "IndexPage", "DeviceIndexPage", "ProjectIndexPage"]


class FlexPage(AbstractFlexPage):
    parent_page_types = ["HomePage", "FolderPage"]
    subpage_type = []

    template = "pages/flex.html"

    body = StreamField(FlexBlock(), blank=True, use_json_field=True)

    content_panels = AbstractHomePage.content_panels + [
        FieldPanel("body"),
    ]


class ArticlePage(AbstractArticlePage):
    parent_page_types = ["IndexPage"]
    subpage_type = []

    template = "pages/article.html"


class IndexPage(AbstractIndexPage):
    parent_page_types = ["HomePage", "FolderPage"]
    subpage_type = ["ArticlePage"]

    template = "pages/index.html"


class ProjectIndexPage(AbstractIndexPage):
    parent_page_types = ["FolderPage", "HomePage"]
    subpage_type = ["ProjectPage"]

    template = "pages/category.html"

    def get_context(self, request):
        context = super().get_context(request)
        all_children = (
            self.get_children().live().specific().order_by("-projectpage__category")
        )
        context["children"] = all_children
        return context

    class Meta:
        verbose_name = "Projekte"


class SearchPage(AbstractSearchPage):
    parent_page_types = ["HomePage"]
    subpage_type = []

    template = "pages/search.html"


class ProjectPageLink(Orderable, Link):
    page = ParentalKey(
        "ProjectPage", on_delete=models.CASCADE, related_name="project_links"
    )


class ProjectPage(AbstractProjectPage):
    template = "pages/project.html"

    parent_page_types = ["ProjectIndexPage"]
    subpage_type = []

    body = StreamField(ProjectBlock(), blank=True, use_json_field=True)

    content_panels = AbstractProjectPage.content_panels + [
        InlinePanel("project_links", label="Project Links"),
        FieldPanel("body"),
    ]


class DeviceIndexPage(AbstractIndexPage):
    parent_page_types = ["FolderPage", "HomePage"]
    subpage_type = [""]

    template = "pages/devices.html"

    def get_context(self, request):
        context = super().get_context(request)
        devices = Device.objects.all()
        context["devices"] = devices
        return context

    class Meta:
        verbose_name = "Geräte"


class CollectionPagePage(Orderable, PageLink):
    page = ParentalKey(
        "CollectionPage", on_delete=models.CASCADE, related_name="collection_pages"
    )


class CollectionPageLink(Orderable, ExpireLink):
    page = ParentalKey(
        "CollectionPage", on_delete=models.CASCADE, related_name="collection_links"
    )


class CollectionPage(AbstractBasePage, ClusterableModel):
    parent_page_types = ["HomePage"]
    subpage_type = []

    template = "pages/collection.html"

    content_panels = AbstractBasePage.content_panels + [
        InlinePanel("collection_links", label="Link", classname="collabsible"),
        InlinePanel("collection_pages", label="Page", classname="collabsible"),
    ]

    class Meta:
        verbose_name = "Link Sammlung"


from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField,
    FORM_FIELD_CHOICES,
)


class FormField(AbstractFormField):
    CHOICES = FORM_FIELD_CHOICES + (("pageParam", "Page Parameter"),)

    page = ParentalKey("FormPage", related_name="form_fields")
    field_type = models.CharField(
        verbose_name="field type",
        max_length=16,
        choices=CHOICES,
    )


from organisation.models import Event
import datetime
from calendar import monthrange


def get_repeated_event(element, year, month, day):
    repeated = []
    count = monthrange(year, month)[1]

    for days in range(count):
        switch = True
        weekday = element.start.weekday()
        current_date = datetime.date(year, month, days + 1)

        for exception in element.related_expection.all():
            if current_date >= exception.start and current_date <= exception.end:
                switch = False

        if weekday == current_date.weekday() and switch and current_date.day >= day:
            repeated.append(current_date.strftime("%d.%m.%Y"))

    return repeated


def get_events(element, year, month, day):
    if element.repeat == "0":
        return
    date = datetime.date(year, month, day)
    events = []

    while len(events) < 3:
        if element.visible_events(date):
            events.extend(get_repeated_event(element, date.year, date.month, date.day))
        date = datetime.date(date.year, date.month, 1) + relativedelta(months=+1)
        if date > element.repeatEnd:
            break

    return ", ".join(events)


class FormPage(FabLabCaptchaEmailForm):
    parent_page_types = ["HomePage", "FolderPage", "FlexPage"]
    subpage_type = []

    content = StreamField(FormBlock(), blank=True, use_json_field=True)

    event = models.ForeignKey(
        "organisation.event",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    response_switch = models.BooleanField(blank=True, null=True)
    response_subject = models.TextField(blank=True, null=True)
    response_message = models.TextField(blank=True, null=True)

    thank_you_text = RichTextField(blank=True)

    content_panels = [
        FieldPanel("event"),
        FieldPanel("content"),
        InlinePanel("form_fields", label="Form Elemente"),
        FieldPanel("thank_you_text", heading="Bestätigung"),
    ]

    email_panels = [
        MultiFieldPanel(
            [
                FieldPanel("response_switch", heading="Switch"),
                FieldPanel("response_subject", heading="Betreff"),
                FieldPanel("response_message", heading="Nachricht"),
            ],
            "Email Antwort",
        ),
        MultiFieldPanel(
            [
                FieldPanel("from_address"),
                FieldPanel("to_address"),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, "Inhalt"),
            ObjectList(email_panels, "Email"),
            ObjectList(AbstractBasePage.promote_panels, "Veröffentlichung"),
        ]
    )

    template = "forms/form_page.html"

    def get_form_fields(self):
        fields = list(super().get_form_fields())
        if self.event == None:
            return fields
        date = datetime.date.today()
        element = Event.objects.get(title=self.event)
        events = get_events(element, date.year, date.month, date.day)
        if events != None:
            fields.insert(
                0,
                FormField(
                    label="Datum",
                    clean_name="date",
                    field_type="dropdown",
                    choices=events,
                    required=True,
                ),
            )
        return fields

    class Meta:
        verbose_name = "Form Seite"
