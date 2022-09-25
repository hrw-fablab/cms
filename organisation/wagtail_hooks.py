from wagtail.admin.viewsets.chooser import ChooserViewSet
from wagtail import hooks

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from .models import (
    Person,
    Project,
    DeviceCategory,
    ProjectCategory,
    Organisation,
    Event,
)


class PersonAdmin(ModelAdmin):
    model = Person
    menu_icon = "user"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "last_name", "organisation", "thumb_image")
    list_filter = ("organisation",)
    search_fields = (
        "first_name",
        "last_name",
        "organisation__name",
        "title",
    )


class ProjectAdmin(ModelAdmin):
    model = Project
    menu_icon = "group"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "Personenanzahl")
    list_filter = ("name",)
    search_fields = ("name",)


class OrganisationAdmin(ModelAdmin):
    model = Organisation
    menu_icon = "group"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "Projektanzahl")
    list_filter = ("name", "related_projects__project")
    search_fields = ("name",)


class OrganisationGroup(ModelAdminGroup):
    menu_label = "Organisation"
    menu_icon = "group"
    menu_order = 200
    items = (PersonAdmin, ProjectAdmin, OrganisationAdmin)


modeladmin_register(OrganisationGroup)


class DeviceAdmin(ModelAdmin):
    model = DeviceCategory
    menu_icon = "tag"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False


class ProjectAdmin(ModelAdmin):
    model = ProjectCategory
    menu_icon = "tag"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False


class CategoryGroup(ModelAdminGroup):
    menu_label = "Kategorien"
    menu_icon = "tag"
    menu_order = 200
    items = (DeviceAdmin, ProjectAdmin)


modeladmin_register(CategoryGroup)


class EventAdmin(ModelAdmin):
    model = Event
    menu_icon = "date"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "adress", "start", "end")
    list_filter = ("start",)
    search_fields = ("title",)


modeladmin_register(EventAdmin)


class PersonChooserViewSet(ChooserViewSet):
    # The model can be specified as either the model class or an "app_label.model_name" string;
    # using a string avoids circular imports when accessing the StreamField block class (see below)
    model = "organisation.Person"

    icon = "user"
    choose_one_text = "Choose a person"
    choose_another_text = "Choose another person"
    edit_item_text = "Edit this person"
    form_fields = ["first_name", "last_name"]


class ProjectChooserViewSet(ChooserViewSet):
    # The model can be specified as either the model class or an "app_label.model_name" string;
    # using a string avoids circular imports when accessing the StreamField block class (see below)
    model = "organisation.Project"

    icon = "user"
    choose_one_text = "Choose a project"
    choose_another_text = "Choose another project"
    edit_item_text = "Edit this project"


class DeviceCategoryChooserViewSet(ChooserViewSet):
    # The model can be specified as either the model class or an "app_label.model_name" string;
    # using a string avoids circular imports when accessing the StreamField block class (see below)
    model = "organisation.DeviceCategory"

    icon = "user"
    choose_one_text = "Choose a device"
    choose_another_text = "Choose another device"
    edit_item_text = "Edit this device"


class ProjectCategoryChooserViewSet(ChooserViewSet):
    # The model can be specified as either the model class or an "app_label.model_name" string;
    # using a string avoids circular imports when accessing the StreamField block class (see below)
    model = "organisation.ProjectCategory"

    icon = "user"
    choose_one_text = "Choose a category"
    choose_another_text = "Choose another category"
    edit_item_text = "Edit this category"


class OrganisationChooserViewSet(ChooserViewSet):
    # The model can be specified as either the model class or an "app_label.model_name" string;
    # using a string avoids circular imports when accessing the StreamField block class (see below)
    model = "organisation.Organisation"

    icon = "user"
    choose_one_text = "Choose a organisation"
    choose_another_text = "Choose another organisation"
    edit_item_text = "Edit this organisation"


person_chooser_viewset = PersonChooserViewSet("person_chooser")
project_chooser_viewset = ProjectChooserViewSet("project_chooser")
organisation_chooser_viewset = OrganisationChooserViewSet("organisation_chooser")
projectcategory_chooser_viewset = ProjectCategoryChooserViewSet(
    "projectcategory_chooser"
)
devicecategory_chooser_viewset = DeviceCategoryChooserViewSet("devicecategory_chooser")


@hooks.register("register_admin_viewset")
def register_viewset():
    return person_chooser_viewset


@hooks.register("register_admin_viewset")
def register_viewset():
    return project_chooser_viewset


@hooks.register("register_admin_viewset")
def register_viewset():
    return organisation_chooser_viewset


@hooks.register("register_admin_viewset")
def register_viewset():
    return projectcategory_chooser_viewset


@hooks.register("register_admin_viewset")
def register_viewset():
    return devicecategory_chooser_viewset
