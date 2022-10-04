from django_components import component


@component.register("heading")
class Heading(component.Component):
    template_name = "heading/heading.html"

    def get_context_data(self, value, anchor):
        print(value)
        return {
            "value": value,
            "url": value.replace(" ", ""),
            "anchor": anchor,
        }

    class Media:
        css = "heading/heading.css"
        js = ""
