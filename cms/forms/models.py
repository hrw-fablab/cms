from __future__ import absolute_import, unicode_literals
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormSubmission
from cms.core.models import FablabBasePage

from .forms import FabLabCaptchaFormBuilder, remove_honeypot_field

from django.db import models
from django.core.mail import send_mail


class FabLabCaptchaEmailForm(AbstractEmailForm, FablabBasePage):
    form_builder = FabLabCaptchaFormBuilder

    def get_submission_class(self):
        return CustomFormSubmission

    def process_form_submission(self, form):
        remove_honeypot_field(form)
        data = form.cleaned_data
        date = None
        if "date" in data:
            date = data["date"]
        submission = self.get_submission_class().objects.create(
            form_data=form.cleaned_data, page=self, date=date
        )
        if self.to_address:
            self.send_mail(form)
        if self.response_switch is True:
            try:
                send_mail(
                    self.response_subject,
                    self.response_message,
                    "",
                    [data["e_mail"]],
                )
            except: # noqa
                pass
        return submission

    class Meta:
        abstract = True


class CustomFormSubmission(AbstractFormSubmission):
    date = models.CharField(max_length=100, blank=True, null=True)

    def get_data(self):
        form_data = super().get_data()
        form_data.update({"date": self.date})

        return form_data
