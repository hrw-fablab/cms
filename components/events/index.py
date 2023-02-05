import datetime
from django_components import component
from organisation.models import Event


def get_events():
    date = datetime.date.today()
    events = []

    print(Event.objects.filter(start__range=["2011-01-01", "2011-01-31"]))

    for element in Event.objects.all():
        print(element)


@component.register("events")
class Events(component.Component):
    template_name = "events/index.html"

    def get_context_data(self):
        return {
            "events": [],
        }

    class Media:
        css = "events/index.css"
        js = "events/index.js"
