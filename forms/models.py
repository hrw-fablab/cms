from wagtail.contrib.forms.models import AbstractEmailForm
from core.models import FablabBasePage

from forms.forms import FabLabCaptchaFormBuilder, remove_captcha_field


class FabLabCaptchaEmailForm(AbstractEmailForm, FablabBasePage):
    """Pages implementing a captcha form with email notification should inhert from this"""

    form_builder = FabLabCaptchaFormBuilder

    def process_form_submission(self, form):
        remove_captcha_field(form)
        return super(FabLabCaptchaEmailForm, self).process_form_submission(form)

    class Meta:
        abstract = True
