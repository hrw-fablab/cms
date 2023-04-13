from django_components import component


@component.register("gallery")
class Gallery(component.Component):
    template_name = "gallery/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "gallery/index.css"
