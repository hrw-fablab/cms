from calendar import monthrange
import datetime
from dateutil.relativedelta import relativedelta
from django_components import component
from events.models import Event
from django.db.models import Q


@component.register("split")
class Split(component.Component):
    template_name = "split/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "split/index.css"
