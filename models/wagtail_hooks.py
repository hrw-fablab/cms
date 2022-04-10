from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Person, Project


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


modeladmin_register(PersonAdmin)
modeladmin_register(ProjectAdmin)
