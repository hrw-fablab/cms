from django import forms
from django.conf import settings
from django.forms.models import modelform_factory
from django.utils.module_loading import import_string
from wagtail.admin import widgets
from wagtailmedia.permissions import permission_policy as media_permission_policy
from wagtail.admin.forms.collections import BaseCollectionMemberForm

from wagtail.images.widgets import AdminImageChooser
from wagtail.admin.staticfiles import versioned_static


class CustomImageChooser(AdminImageChooser):
    @property
    def media(self):
        return forms.Media(
            js=[
                versioned_static("wagtailadmin/js/modal-workflow.js"),
                versioned_static("wagtailimages/js/image-chooser-modal.js"),
                versioned_static("wagtailimages/js/image-chooser.js"),
            ]
        )


class FabLabMediaForm(BaseCollectionMemberForm):
    class Meta:
        widgets = {
            "tags": widgets.AdminTagWidget,
            "file": forms.FileInput,
            "thumbnail": forms.ClearableFileInput,
            "preview": CustomImageChooser,
        }

    permission_policy = media_permission_policy

    def __init__(self, *args, **kwargs):
        super(FabLabMediaForm, self).__init__(*args, **kwargs)

        if self.instance.type == "audio":
            for name in ("width", "height"):
                # these fields might be editable=False so verify before accessing
                if name in self.fields:
                    del self.fields[name]


def get_media_base_form():
    base_form_override = getattr(settings, "WAGTAILMEDIA_MEDIA_FORM_BASE", "")
    if base_form_override:
        base_form = import_string(base_form_override)
    else:
        base_form = FabLabMediaForm
    return base_form


def get_media_form(model):
    fields = model.admin_form_fields
    if "collection" not in fields:
        # force addition of the 'collection' field, because leaving it out can
        # cause dubious results when multiple collections exist (e.g adding the
        # media to the root collection where the user may not have permission) -
        # and when only one collection exists, it will get hidden anyway.
        fields = list(fields) + ["collection"]

    return modelform_factory(
        model,
        form=media_base_form,
        fields=fields,
    )


media_base_form = get_media_base_form()
