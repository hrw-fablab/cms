from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from abstract.pages.article import AbstractArticlePage

from abstract.pages.home import AbstractHomePage
from abstract.pages.folder import AbstractFolderPage
from abstract.pages.index import AbstractIndexPage
from .blocks import StructBlock

class HomePage(AbstractHomePage):
	template = "pages/home.html"

	body = StreamField(StructBlock())

	content_panels = Page.content_panels + [
		StreamFieldPanel("body"),
	]

class FolderPage(AbstractFolderPage):
	parent_page_types = ["Homepage"]
	subpage_type = ["ArticleIndexPage"]

class ArticleIndexPage(AbstractIndexPage):
	template = "pages/index.html"
	
	parent_page_types = ["FolderPage", "HomePage"]
	subpage_type = ["ArticlePage"]

	def get_context(self, request):
		context = super().get_context(request)
		children = ArticlePage.objects.live().public().order_by('-last_published_at')
		context["children"] = children

		if request.GET.get('author'):
			children = ArticlePage.objects.live().public().filter(author__last_name=request.GET.get('author')).order_by('-last_published_at')
			context["children"] = children
		
		if request.GET.get('tag'):
			children = ArticlePage.objects.live().public().filter(tag__name=request.GET.get('tag')).order_by('-last_published_at')
			context["children"] = children
		return context

class ArticlePage(AbstractArticlePage):
	template = "pages/article.html"

	def get_context(self, request):
		context = super().get_context(request)
		parent = Page.get_parent(self)
		context["parent"] = parent
		return context
	
	parent_page_types = ["ArticleIndexPage"]
	subpage_type = []