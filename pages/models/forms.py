from dateutil.relativedelta import relativedelta
from django.db import models
from django.shortcuts import redirect

from core.models import FablabBasePage

from wagtail.admin.panels import (
    InlinePanel,
    FieldPanel,
    MultiFieldPanel,
    TabbedInterface,
    ObjectList,
)

from modelcluster.fields import ParentalKey

from forms.models import FabLabCaptchaEmailForm
from blocks.models import FormBlock

from wagtail.fields import RichTextField, StreamField
from wagtail.contrib.forms.models import AbstractFormField, FORM_FIELD_CHOICES
from wagtail.contrib.routable_page.models import RoutablePageMixin, path


class FormField(AbstractFormField):
    CHOICES = FORM_FIELD_CHOICES + (("pageParam", "Page Parameter"),)

    page = ParentalKey("FormPage", related_name="form_fields")
    field_type = models.CharField(
        verbose_name="field type",
        max_length=16,
        choices=CHOICES,
    )


from events.models import Event
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


class FormPage(RoutablePageMixin, FabLabCaptchaEmailForm):
    parent_page_types = ["HomePage", "FolderPage", "FlexPage"]
    subpage_type = []

    content = StreamField(FormBlock(), blank=True, use_json_field=True)

    event = models.ForeignKey(
        "events.event",
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
        FieldPanel("title"),
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
            ObjectList(FablabBasePage.promote_panels, "Veröffentlichung"),
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

    @path("")
    def index_route(self, request, *args, **kwargs):
        return super(FabLabCaptchaEmailForm, self).serve(request, *args, **kwargs)

    def render_landing_page(self, request, form_submission, *args, **kwargs):
        url = self.reverse_subpage("thank_you")
        return redirect(self.url + url, permanent=False)

    @path("thank-you/")
    def thank_you(self, request):
        form_submission = None
        try:
            submission_id = int(request.GET["id"])
        except (KeyError, TypeError):
            pass
        else:
            submission_class = self.get_submission_class()
            try:
                form_submission = submission_class.objects.get(id=submission_id)
            except submission_class.DoesNotExist:
                pass

        return super().render_landing_page(request, form_submission)

    class Meta:
        verbose_name = "Form Seite"
