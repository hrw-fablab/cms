from django_components import component


@component.register("grid")
class Grid(component.Component):
    template_name = "grid/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "grid/index.css"
