from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from .models import Person, Project, DeviceCategory, ProjectCategory

from wagtail.core import hooks

from wagtail.core.models import TranslatableMixin

from .view import PersonChooserViewSet, ProjectChooserViewSet, DeviceCategoryChooserViewSet, ProjectCategoryChooserViewSet

@hooks.register("register_admin_viewset")
def register_person_chooser_viewset():
    return PersonChooserViewSet("person_chooser", url_prefix="person-chooser")


@hooks.register("register_admin_viewset")
def register_project_chooser_viewset():
    return ProjectChooserViewSet("project_chooser", url_prefix="project-chooser")

@hooks.register("register_admin_viewset")
def register_devicecategory_chooser_viewset():
    return DeviceCategoryChooserViewSet("devicecategory_chooser", url_prefix="devicecategory-chooser")

@hooks.register("register_admin_viewset")
def register_projectcategory_chooser_viewset():
    return ProjectCategoryChooserViewSet("projectcategory_chooser", url_prefix="projectcategory-chooser")


class PersonAdmin(ModelAdmin, TranslatableMixin):
    model = Person
    menu_icon = "user"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("first_name", "last_name", "employment", "thumb_image")
    list_filter = ("first_name", "last_name", "employment", "since")
    search_fields = ("first_name", "last_name")


class ProjectAdmin(ModelAdmin, TranslatableMixin):
    model = Project
    menu_icon = "group"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)
    list_filter = ("name", "related_member__person")
    search_fields = ("name",)


class OrganisationGroup(ModelAdminGroup):
    menu_label = "Organisation"
    menu_icon = "group"
    menu_order = 200
    items = (PersonAdmin, ProjectAdmin)


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
