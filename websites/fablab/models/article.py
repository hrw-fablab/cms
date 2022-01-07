from wagtail.core.models import Page
from abstract.pages.article import AbstractArticlePage

class ArticlePage(AbstractArticlePage):
	parent_page_types = ["ArticleIndexPage"]
	subpage_type = []

	template = "pages/article.html"

	def get_context(self, request):
		context = super().get_context(request)
		parent = Page.get_parent(self)
		context["parent"] = parent
		return context