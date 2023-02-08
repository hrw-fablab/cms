from wagtail.admin.viewsets.chooser import ChooserViewSet
from wagtail import hooks

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from .models import (
    Person,
)


class PersonAdmin(ModelAdmin):
    model = Person
    menu_icon = "user"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "last_name", "thumb_image")
    search_fields = (
        "first_name",
        "last_name",
        "title",
    )


modeladmin_register(PersonAdmin)


class PersonChooserViewSet(ChooserViewSet):
    # The model can be specified as either the model class or an "app_label.model_name" string;
    # using a string avoids circular imports when accessing the StreamField block class (see below)
    model = "persons.Person"

    icon = "user"
    choose_one_text = "Choose a person"
    choose_another_text = "Choose another person"
    edit_item_text = "Edit this person"
    form_fields = ["first_name", "last_name"]


person_chooser_viewset = PersonChooserViewSet("person_chooser")


@hooks.register("register_admin_viewset")
def register_viewset():
    return person_chooser_viewset
