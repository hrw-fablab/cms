from organisation.wagtail_hooks import (
    person_chooser_viewset,
    project_chooser_viewset,
    organisation_chooser_viewset,
)

PersonChooserBlock = person_chooser_viewset.get_block_class(
    name="PersonChooserBlock", module_path="abstract.blocks"
)

ProjectChooserBlock = project_chooser_viewset.get_block_class(
    name="ProjectChooserBlock", module_path="abstract.blocks"
)

OrganizationChooserBlock = organisation_chooser_viewset.get_block_class(
    name="OrganizationChooserBlock", module_path="abstract.blocks"
)
