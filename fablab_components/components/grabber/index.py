from django_components import component

@component.register("grabber")
class Grabber(component.Component):
    template_name = "grabber/index.html"

    def get_context_data(self, title):
        return {"title": title}

    class Media:
        css = "grabber/index.css"
        js = "grabber/index.js"
