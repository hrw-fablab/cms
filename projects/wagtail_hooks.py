from wagtail.admin.viewsets.chooser import ChooserViewSet
from wagtail import hooks

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Project


class ProjectAdmin(ModelAdmin):
    model = Project
    menu_icon = "tag"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False


modeladmin_register(ProjectAdmin)


class ProjectChooserViewSet(ChooserViewSet):
    # The model can be specified as either the model class or an "app_label.model_name" string;
    # using a string avoids circular imports when accessing the StreamField block class (see below)
    model = "projects.Project"

    icon = "user"
    choose_one_text = "Choose a project"
    choose_another_text = "Choose another project"
    edit_item_text = "Edit this project"


project_chooser_viewset = ProjectChooserViewSet("project_chooser")


@hooks.register("register_admin_viewset")
def register_viewset():
    return project_chooser_viewset
