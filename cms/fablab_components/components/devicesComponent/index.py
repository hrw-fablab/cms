from django_components import component


@component.register("devicesComponent")
class DevicesComponent(component.Component):
    template_name = "devicesComponent/index.html"

    def get_context_data(self, devices):
        return {
            "devices": devices,
        }

    class Media:
        css = "devicesComponent/index.css"
        js = "devicesComponent/index.js"
