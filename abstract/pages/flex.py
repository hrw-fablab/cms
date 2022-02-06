from core.models import FablabBasePage


class AbstractFlexPage(FablabBasePage):
    class Meta:
        verbose_name = "Flexible Seite"
        abstract = True
