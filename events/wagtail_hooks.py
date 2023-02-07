from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Event


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
