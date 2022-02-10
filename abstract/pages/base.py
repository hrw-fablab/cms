from core.models import FablabBasePage


class AbstractBasePage(FablabBasePage):
    class Meta:
        verbose_name = "Überschreibe diesen Namen"
        abstract = True
