from __future__ import absolute_import, unicode_literals

from wagtail.contrib.forms.forms import FormBuilder
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

from django import forms

class FabLabCaptchaFormBuilder(FormBuilder):
    CAPTCHA_FIELD_NAME = "wagtailcaptcha"

    def create_hiddenDate_field(self, field, options):
        # return `forms.GenericIPAddressField(**options)` not `forms.SlugField`
        # returns created a form field with the options passed in
        return forms.CharField(**options)

    @property
    def formfields(self):
        # Add wagtailcaptcha to formfields property
        fields = super(FabLabCaptchaFormBuilder, self).formfields
        fields[self.CAPTCHA_FIELD_NAME] = ReCaptchaField(label="", widget=ReCaptchaV3())
        return fields

def remove_captcha_field(form):
    form.fields.pop(FabLabCaptchaFormBuilder.CAPTCHA_FIELD_NAME, None)
    form.cleaned_data.pop(FabLabCaptchaFormBuilder.CAPTCHA_FIELD_NAME, None)
