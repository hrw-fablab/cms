from django_components import component


@component.register("embed")
class Embed(component.Component):
    template_name = "embed/index.html"

    def get_context_data(self, url, title):
        return {"url": url, "title": title}

    class Media:
        css = "embed/index.css"
