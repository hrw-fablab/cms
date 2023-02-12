from django_components import component


@component.register("project")
class Project(component.Component):
    template_name = "project/index.html"

    def get_context_data(self, title):
        return {"title": title}

    class Media:
        css = "project/index.css"
        js = "project/index.js"
