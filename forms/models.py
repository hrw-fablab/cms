from __future__ import absolute_import, unicode_literals
from regex import B

from wagtail.contrib.forms.models import AbstractEmailForm
from core.models import FablabBasePage

from forms.forms import FabLabCaptchaFormBuilder, remove_captcha_field

import datetime
import os

from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.core.validators import validate_email
from django.db import models
from django.template.response import TemplateResponse
from django.utils.formats import date_format
from django.utils.translation import gettext_lazy as _

from wagtail.admin.mail import send_mail
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.forms.utils import get_field_clean_name
from wagtail.models import Orderable, Page


class FabLabCaptchaEmailForm(AbstractEmailForm, FablabBasePage):
    """Pages implementing a captcha form with email notification should inhert from this"""

    form_builder = FabLabCaptchaFormBuilder

    def get_submission_class(self):
        return CustomFormSubmission

    def serve(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.get_form(
                request.POST, request.FILES, page=self, user=request.user
            )

            if form.is_valid():
                form_submission = self.process_form_submission(
                    form, request.POST.get("this_test")
                )
                return self.render_landing_page(
                    request, form_submission, *args, **kwargs
                )
        else:
            form = self.get_form(page=self, user=request.user)

        context = self.get_context(request)
        context["form"] = form
        return TemplateResponse(request, self.get_template(request), context)


    def process_form_submission(self, form, date):
        data = form.cleaned_data
        submission = self.get_submission_class().objects.create(
            form_data=form.cleaned_data,
            page=self,
            date=data['date']
        )
        if self.to_address:
            self.send_mail(form, date)
        return submission

    def send_mail(self, form, date):
        addresses = [x.strip() for x in self.to_address.split(",")]
        send_mail(
            self.subject,
            self.render_email(form, date),
            addresses,
            self.from_address,
        )

    def render_email(self, form, date):
        content = []

        cleaned_data = form.cleaned_data
        for field in form:
            if field.name not in cleaned_data:
                continue

            value = cleaned_data.get(field.name)

            if isinstance(value, list):
                value = ", ".join(value)

            # Format dates and datetimes with SHORT_DATE(TIME)_FORMAT
            if isinstance(value, datetime.datetime):
                value = date_format(value, settings.SHORT_DATETIME_FORMAT)
            elif isinstance(value, datetime.date):
                value = date_format(value, settings.SHORT_DATE_FORMAT)

            content.append("{}: {}".format(field.label, value))

        content.append(date)

        return "\n".join(content)

    class Meta:
        abstract = True

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, AbstractFormSubmission

class CustomFormSubmission(AbstractFormSubmission):
    form_data = models.JSONField(encoder=DjangoJSONEncoder)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    date = models.CharField(max_length=100, blank=True)

    submit_time = models.DateTimeField(verbose_name=_("submit time"), auto_now_add=True)

    def get_data(self):
        form_data = super().get_data()
        form_data.update({
            'date': self.date
        })

        return form_data

    def __str__(self):
        return self.form_data
