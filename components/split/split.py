from django_components import component


@component.register("split")
class Split(component.Component):
    template_name = "split/split.html"

    def get_context_data(self, image, title, text):
        return {
            "image": image,
            "title": title,
            "text": text,
        }

    class Media:
        css = "split/split.css"
        js = ""
