from abstract.pages.device import AbstractDevicePage

class DevicePage(AbstractDevicePage):
	template = "pages/article.html"

	parent_page_types = ["DeviceIndexPage"]
	subpage_type = []