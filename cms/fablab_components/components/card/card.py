from django_components import component


@component.register("card")
class Card(component.Component):
    template_name = "card/card.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self, style, title, text, link, image, date, author):
        return {
            "style": style,
            "title": title,
            "text": text,
            "link": link,
            "image": image,
            "date": date,
            "author": author,
        }

    class Media:
        css = "card/card.css"
