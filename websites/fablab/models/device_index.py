from abstract.pages.index import AbstractIndexPage
from .device import DevicePage

class DeviceIndexPage(AbstractIndexPage):
	template = "pages/category.html"
	
	parent_page_types = ["FolderPage", "HomePage"]
	subpage_type = ["DevicePage"]

	def get_context(self, request):
		context = super().get_context(request)
		children = DevicePage.objects.live().public().child_of(self).order_by('-last_published_at')
		context["children"] = children
		return context
