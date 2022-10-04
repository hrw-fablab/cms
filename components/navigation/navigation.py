from django_components import component


@component.register("navigation")
class Navigation(component.Component):
    template_name = "navigation/navigation.html"

    class Media:
        css = "navigation/navigation.css"
        js = ""
