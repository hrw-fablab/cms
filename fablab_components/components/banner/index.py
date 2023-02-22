from calendar import monthrange
import datetime
from dateutil.relativedelta import relativedelta
from django_components import component
from events.models import Event
from django.db.models import Q


@component.register("banner")
class Banner(component.Component):
    template_name = "banner/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "banner/index.css"
        js = "banner/index.js"
