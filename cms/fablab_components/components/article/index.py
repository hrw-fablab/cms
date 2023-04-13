from calendar import monthrange
import datetime
from dateutil.relativedelta import relativedelta
from django_components import component
from events.models import Event
from django.db.models import Q


@component.register("article")
class Article(component.Component):
    template_name = "article/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "article/index.css"
