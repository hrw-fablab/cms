from persons.wagtail_hooks import person_chooser_viewset
from projects.wagtail_hooks import project_chooser_viewset

PersonChooserBlock = person_chooser_viewset.get_block_class(
    name="PersonChooserBlock", module_path="blocks.blocks"
)

ProjectChooserBlock = project_chooser_viewset.get_block_class(
    name="ProjectChooserBlock", module_path="blocks.blocks"
)
