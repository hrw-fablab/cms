from wagtail.admin.viewsets.chooser import ChooserViewSet
from wagtail import hooks

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

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


class EventChooserViewSet(ChooserViewSet):
    # The model can be specified as either the model class or an "app_label.model_name" string;
    # using a string avoids circular imports when accessing the StreamField block class (see below)
    model = "events.Event"

    icon = "date"
    choose_one_text = "Choose a event"
    choose_another_text = "Choose another event"
    edit_item_text = "Edit this event"


event_chooser_viewset = EventChooserViewSet("event_chooser")


@hooks.register("register_admin_viewset")
def register_viewset():
    return event_chooser_viewset
