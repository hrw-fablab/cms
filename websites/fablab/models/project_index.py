from abstract.pages.index import AbstractIndexPage
from .project import ProjectPage

class ProjectIndexPage(AbstractIndexPage):
	template = "pages/projects.html"
	
	parent_page_types = ["FolderPage", "HomePage"]
	subpage_type = ["ProjectPage"]

	def get_context(self, request):
		context = super().get_context(request)
		children = ProjectPage.objects.live().public().child_of(self).order_by('-last_published_at')
		context["children"] = children
		return context