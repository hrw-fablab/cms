from django_components import component


@component.register("article")
class Article(component.Component):
    template_name = "article/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "article/index.css"
