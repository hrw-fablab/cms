from calendar import monthrange
import datetime
from dateutil.relativedelta import relativedelta
from django_components import component
from events.models import Event
from django.db.models import Q


@component.register("calendar")
class Calendar(component.Component):
    template_name = "calendar/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "calendar/index.css"
        js = "calendar/index.js"
