from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from wagtail.core import hooks

from .views import PersonChooserViewSet, ProjectChooserViewSet, DeviceCategoryChooserViewSet, ProjectCategoryChooserViewSet, OrganisationChooserViewSet


@hooks.register("register_admin_viewset")
def register_person_chooser_viewset():
    return PersonChooserViewSet("person_chooser", url_prefix="person-chooser")

@hooks.register("register_admin_viewset")
def register_person_edit_viewset():
    return PersonChooserViewSet("person_edit", url_prefix="person-edit")

@hooks.register("register_admin_viewset")
def register_project_chooser_viewset():
    return ProjectChooserViewSet("project_chooser", url_prefix="project-chooser")

@hooks.register("register_admin_viewset")
def register_devicecategory_chooser_viewset():
    return DeviceCategoryChooserViewSet("devicecategory_chooser", url_prefix="devicecategory-chooser")

@hooks.register("register_admin_viewset")
def register_projectcategory_chooser_viewset():
    return ProjectCategoryChooserViewSet("projectcategory_chooser", url_prefix="projectcategory-chooser")

@hooks.register("register_admin_viewset")
def register_organisation_chooser_viewset():
    return OrganisationChooserViewSet("organisation_chooser", url_prefix="organisation-chooser")
