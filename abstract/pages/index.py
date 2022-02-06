from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page

from core.models import FablabBasePage


from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.core.models import Page

class AbstractIndexPage(FablabBasePage):
    heading = models.CharField(max_length=255, blank=True)

    content_panels = FablabBasePage.content_panels + [
        FieldPanel("heading"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        all_children = (
            self.childrenPage.
            objects.
            live().
            public().
            child_of(self).
            specific().
            order_by("-last_published_at")
        )

        if request.GET.get("author"):
            all_children = all_children.filter(author__last_name=request.GET.get("author")).order_by("-last_published_at")
        
        if request.GET.get("tag"):
            all_children = all_children.filter(tag__name=request.GET.get("tag")).order_by("-last_published_at")
        
        paginator = Paginator(all_children, 8)
        page = request.GET.get("page")
        try:
            children = paginator.page(page)
        except PageNotAnInteger:
            children = paginator.page(1)
        except EmptyPage:
            children = paginator.page(paginator.num_pages)
        context["children"] = children
        
        return context
    class Meta:
        verbose_name = "Index Seite"
        abstract = True
