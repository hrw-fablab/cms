from django.db import models
from wagtail.admin.panels import FieldPanel

from core.models import FablabBasePage


from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class IndexPage(FablabBasePage):
    heading = models.CharField(max_length=255, blank=True)

    content_panels = FablabBasePage.content_panels + [
        FieldPanel("heading"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        all_children = (
            self.get_children().live().specific().order_by("-articlepage__date")
        )

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
