from django_components import component


@component.register("blockquote")
class Blockquote(component.Component):
    template_name = "blockquote/index.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "blockquote/index.css"
