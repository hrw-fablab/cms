from django_components import component


@component.register("call")
class Call(component.Component):
    template_name = "call/index.html"

    def get_context_data(self, title, description, link, link_text):
        return {
            "title": title,
            "description": description,
            "link": link,
            "link_text": link_text,
        }

    class Media:
        css = "call/index.css"
        js = "call/index.js"
