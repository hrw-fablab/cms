from django_components import component


@component.register("person")
class Person(component.Component):
    template_name = "person/index.html"

    def get_context_data(self, title, firstname, lastname, image, link, area):
        return {
            "title": title,
            "firstname": firstname,
            "lastname": lastname,
            "image": image,
            "link": link,
            "area": area,
        }

    class Media:
        css = "person/index.css"
