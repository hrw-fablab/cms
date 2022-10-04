from django_components import component


@component.register("footer")
class Footer(component.Component):
    template_name = "footer/footer.html"

    class Media:
        css = "footer/footer.css"
        js = ""
