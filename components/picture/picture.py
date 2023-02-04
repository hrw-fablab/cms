from django_components import component


def getImageRendition(image, sizes, imageQuality, imageFormat):
    results = []
    for index, item in enumerate(sizes):
        renditionParam = f"fill-{sizes[index]}|{imageFormat}|{imageQuality}"
        rendition = image.get_rendition(renditionParam)
        sizeParam = sizes[index].split("x")
        results.append(f"{rendition.url} {sizeParam[1]}w")

    return ", ".join(results)


def getBreakPoints(breakpoints):
    results = []
    for index, item in enumerate(breakpoints):
        results.append(f"(min-width: {breakpoints[index]}px) {breakpoints[index]}px")

    print(results)
    return " ,".join(results)


@component.register("picture")
class Picture(component.Component):
    template_name = "picture/picture.html"

    def get_context_data(self, image, caption, sizes, breakpoints):
        return {
            "image": image,
            "caption": caption,
            "renditions": getImageRendition(
                image, sizes.split(), "webpquality-80", "format-webp"
            ),
            "breakpoints": getBreakPoints(breakpoints.split()),
        }

    class Media:
        css = "picture/picture.css"
        js = ""
