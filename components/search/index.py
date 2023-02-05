from django_components import component


@component.register("search")
class Search(component.Component):
    template_name = "search/index.html"

    def get_context_data(
        self,
    ):
        return {}

    class Media:
        css = "search/index.css"
        js = "search/index.js"
