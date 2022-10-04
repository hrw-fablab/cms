from django_components import component


@component.register("hero")
class Hero(component.Component):
    template_name = "hero/hero.html"

    def get_context_data(self, title, text, image, links):
        return {"title": title, "text": text, "image": image, "links": links}

    class Media:
        css = "hero/hero.css"
        js = ""
