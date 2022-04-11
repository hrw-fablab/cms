from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from .models import Person, Project, DeviceCategory, ProjectCategory

from wagtail.core import hooks

from .view import PersonChooserViewSet


@hooks.register("register_admin_viewset")
def register_person_chooser_viewset():
    return PersonChooserViewSet("person_chooser", url_prefix="person-chooser")


class PersonAdmin(ModelAdmin):
    model = Person
    menu_label = "Person"
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("first_name", "last_name")
    list_filter = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")


class ProjectAdmin(ModelAdmin):
    model = Project
    menu_label = "Project"
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False


class OrganisationGroup(ModelAdminGroup):
    menu_label = "Organisation"
    menu_icon = "folder-open-inverse"
    menu_order = 200
    items = (PersonAdmin, ProjectAdmin)


modeladmin_register(OrganisationGroup)


class DeviceAdmin(ModelAdmin):
    model = DeviceCategory
    menu_label = "Gerätekategorie"
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False


class ProjectAdmin(ModelAdmin):
    model = ProjectCategory
    menu_label = "Projektkategorien"
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False


class CategoryGroup(ModelAdminGroup):
    menu_label = "Kategorien"
    menu_icon = "folder-open-inverse"
    menu_order = 200
    items = (DeviceAdmin, ProjectAdmin)


modeladmin_register(CategoryGroup)
