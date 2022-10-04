from django_components import component


@component.register("grid")
class Grid(component.Component):
    template_name = "grid/grid.html"

    def get_context_data(self, width, layout, gap):
        return {
            "width": width,
            "layout": layout,
            "gap": gap,
        }

    class Media:
        css = "grid/grid.css"
        js = ""
