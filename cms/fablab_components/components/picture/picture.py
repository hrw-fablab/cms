from django_components import component


def width_rendition(index, format, quality):
    return f"fill-{index}|{format}|{quality}"


def height_width_rendition(index, format, quality):
    return f"height-{index}|{format}|{quality}"


def getImageRendition(image, sizes, imageQuality, imageFormat):
    results = []
    for index, item in enumerate(sizes):
        size = sizes[index]
        params = size.split("x")

        if len(params) > 1:
            renditionParam = width_rendition(size, imageFormat, imageQuality)
            sizeParam = params[1]

        if len(params) == 1:
            renditionParam = height_width_rendition(
                params[0], imageFormat, imageQuality
            )
            sizeParam = params[0]

        rendition = image.get_rendition(renditionParam)
        results.append(f"{rendition.url} {sizeParam}w")

    return ", ".join(results)


def getBreakPoints(breakpoints):
    results = []
    for index, item in enumerate(breakpoints):
        results.append(f"(min-width: {breakpoints[index]}px) {breakpoints[index]}px")

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
        pass
