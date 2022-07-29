from __future__ import absolute_import, unicode_literals

from wagtail.contrib.forms.forms import FormBuilder
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

from django import forms
from django.http import JsonResponse
import json
import datetime
from calendar import monthrange
from organisation.models import Event


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

        if weekday == current_date.weekday() and switch and current_date.day > day:
            repeated.append((current_date, current_date))

    return repeated


def get_events(element, year, month):
    date = datetime.date(year, month + 1, 1)
    events = []

    while len(events) < 3:
        if (
            element.visible_year(date)
            and element.visible_month(date)
            and element.visible_day(date)
        ):
            events.extend(get_repeated_event(element, date.year, date.month, date.day))

    return events


class FabLabCaptchaFormBuilder(FormBuilder):
    CAPTCHA_FIELD_NAME = "wagtailcaptcha"

    def create_pageParam_field(self, field, options):
        date = datetime.date.today()
        element = Event.objects.get(title="Offener Abend")
        options["choices"] = get_events(element, date.year, date.month)
        return forms.ChoiceField(**options)

    @property
    def formfields(self):
        # Add wagtailcaptcha to formfields property
        fields = super(FabLabCaptchaFormBuilder, self).formfields
        fields[self.CAPTCHA_FIELD_NAME] = ReCaptchaField(label="", widget=ReCaptchaV3())
        return fields


def remove_captcha_field(form):
    form.fields.pop(FabLabCaptchaFormBuilder.CAPTCHA_FIELD_NAME, None)
    form.cleaned_data.pop(FabLabCaptchaFormBuilder.CAPTCHA_FIELD_NAME, None)
