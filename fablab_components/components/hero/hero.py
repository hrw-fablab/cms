from django_components import component


@component.register("hero")
class Hero(component.Component):
    template_name = "hero/hero.html"

    def get_context_data(self, title, text, image, video):
        return {
            "title": title,
            "text": text,
            "image": image,
            "video": video,
        }

    class Media:
        css = "hero/hero.css"
        js = "hero/hero.js"
