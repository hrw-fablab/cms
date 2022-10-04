from django_components import component


@component.register("header")
class Header(component.Component):
    template_name = "header/header.html"

    class Media:
        css = "header/header.css"
        js = ""
