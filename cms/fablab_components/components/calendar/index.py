from django_components import component


@component.register("calendar")
class Calendar(component.Component):
    template_name = "calendar/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "calendar/index.css"
        js = "calendar/index.js"
