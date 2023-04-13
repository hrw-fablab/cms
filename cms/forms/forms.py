from __future__ import absolute_import, unicode_literals

from wagtail.contrib.forms.forms import FormBuilder
from django.core.exceptions import ValidationError

from django import forms
import datetime
from calendar import monthrange

import re


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


def validate_even(value):
    pattern = re.compile(
        "((?:(?<=[^a-zA-Z0-9]){0,}(?:(?:https?\:\/\/){0,1}(?:[a-zA-Z0-9\%]{1,}\:[a-zA-Z0-9\%]{1,}[@]){,1})(?:(?:\w{1,}\.{1}){1,5}(?:(?:[a-zA-Z]){1,})|(?:[a-zA-Z]{1,}\/[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\:[0-9]{1,4}){1})){1}(?:(?:(?:\/{0,1}(?:[a-zA-Z0-9\-\_\=\-]){1,})*)(?:[?][a-zA-Z0-9\=\%\&\_\-]{1,}){0,1})(?:\.(?:[a-zA-Z0-9]){0,}){0,1})"
    )
    data = re.search(pattern, value)
    if data is None:
        return
    raise ValidationError("")


class HoneypotField(forms.BooleanField):
    default_widget = forms.CheckboxInput(attrs={"tabindex": "-1"})

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", HoneypotField.default_widget)
        kwargs["required"] = False
        super().__init__(*args, **kwargs)

    def clean(self, value):
        if cleaned_value := super().clean(value):
            raise ValidationError("")
        else:
            return cleaned_value


class FabLabCaptchaFormBuilder(FormBuilder):
    HONEYPOT_FIELD_NAME = "password"

    def create_multiline_field(self, field, options):
        attrs = {"cols": "40", "rows": "5"}
        return forms.CharField(
            widget=forms.Textarea(attrs=attrs), validators=[validate_even], **options
        )

    @property
    def formfields(self):
        fields = super(FabLabCaptchaFormBuilder, self).formfields
        fields[self.HONEYPOT_FIELD_NAME] = HoneypotField()
        return fields


def remove_honeypot_field(form):
    form.fields.pop(FabLabCaptchaFormBuilder.HONEYPOT_FIELD_NAME, None)
    form.cleaned_data.pop(FabLabCaptchaFormBuilder.HONEYPOT_FIELD_NAME, None)
