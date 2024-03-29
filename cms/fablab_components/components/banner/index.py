from django_components import component


@component.register("banner")
class Banner(component.Component):
    template_name = "banner/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "banner/index.css"
