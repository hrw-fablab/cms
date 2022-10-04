from django_components import component


@component.register("hero")
class Hero(component.Component):
    template_name = "hero/hero.html"

    class Media:
        css = "hero/hero.css"
        js = ""
