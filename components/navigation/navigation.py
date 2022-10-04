from django_components import component


@component.register("person")
class Person(component.Component):
    template_name = "person/person.html"

    def get_context_data(self, image, name, role, responsibility):
        return {
            "image": image,
            "name": name,
            "role": role,
            "responsibility": responsibility,
        }

    class Media:
        css = "person/person.css"
        js = ""
