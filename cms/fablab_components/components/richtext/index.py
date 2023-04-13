from django_components import component


@component.register("richtext")
class Richtext(component.Component):
    template_name = "richtext/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "richtext/index.css"
