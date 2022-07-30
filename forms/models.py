from __future__ import absolute_import, unicode_literals

from wagtail.contrib.forms.models import AbstractEmailForm
from core.models import FablabBasePage

from forms.forms import FabLabCaptchaFormBuilder

from django.db import models
from django.utils.translation import gettext_lazy as _

class FabLabCaptchaEmailForm(AbstractEmailForm, FablabBasePage):
    """Pages implementing a captcha form with email notification should inhert from this"""

    form_builder = FabLabCaptchaFormBuilder

    def get_submission_class(self):
        return CustomFormSubmission

    def process_form_submission(self, form):
        data = form.cleaned_data
        submission = self.get_submission_class().objects.create(
            form_data=form.cleaned_data,
            page=self,
            date=data['date']
        )
        if self.to_address:
            self.send_mail(form)
        return submission

    class Meta:
        abstract = True

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormSubmission

class CustomFormSubmission(AbstractFormSubmission):
    date = models.CharField(max_length=100, blank=True)

    def get_data(self):
        form_data = super().get_data()
        form_data.update({
            'date': self.date
        })

        return form_data