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
