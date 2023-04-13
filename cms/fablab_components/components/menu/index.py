from django_components import component


@component.register("menu")
class Grabber(component.Component):
    template_name = "menu/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "menu/index.css"
