from django_components import component


@component.register("navigation")
class Navigation(component.Component):
    template_name = "navigation/navigation.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "navigation/navigation.css"
        js = "navigation/navigation.js"
