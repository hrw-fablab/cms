from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from .models import Person, Project, DeviceCategory, ProjectCategory, Organisation


class PersonAdmin(ModelAdmin):
    model = Person
    menu_icon = "user"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("first_name", "last_name", "organisation", "employment", "thumb_image")
    list_filter = ("organisation", "employment", "since")
    search_fields = ("first_name", "last_name", "organisation", "employment")


class ProjectAdmin(ModelAdmin):
    model = Project
    menu_icon = "group"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "Personenanzahl", "asdf")
    list_filter = ("name", "related_member__person")
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
