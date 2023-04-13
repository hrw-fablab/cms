from django_components import component


@component.register("split")
class Split(component.Component):
    template_name = "split/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "split/index.css"
