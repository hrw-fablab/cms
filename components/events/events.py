from django_components import component


@component.register("events")
class Events(component.Component):
    template_name = "events/events.html"

    class Media:
        css = "events/events.css"
        js = "events/events.js"
