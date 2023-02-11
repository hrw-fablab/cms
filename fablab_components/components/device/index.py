from django_components import component


@component.register("device")
class Device(component.Component):
    template_name = "device/index.html"

    def get_context_data(self, title, model, area, manufacturer, amount, image):
        return {
            "title": title,
            "model": model,
            "area": area,
            "manufacturer": manufacturer,
            "amount": amount,
            "image": image,
        }

    class Media:
        css = "device/index.css"
        js = "device/index.js"
