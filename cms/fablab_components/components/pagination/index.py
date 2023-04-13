from django_components import component


@component.register("pagination")
class Grabber(component.Component):
    template_name = "pagination/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "pagination/index.css"
