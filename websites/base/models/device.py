from abstract.pages.device import AbstractDevicePage


class DevicePage(AbstractDevicePage):
    template = "pages/device.html"

    parent_page_types = ["IndexCategoryPage"]
    subpage_type = []