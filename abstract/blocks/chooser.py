from functools import cached_property
from wagtail import blocks


class ProjectChooserBlock(blocks.ChooserBlock):
    @cached_property
    def target_model(self):
        from organisation.models import Project

        return Project

    @cached_property
    def widget(self):
        from organisation.widgets import ProjectChooser

        return ProjectChooser()

    def get_form_state(self, value):
        return self.widget.get_value_data(value)


class PersonChooserBlock(blocks.ChooserBlock):
    @cached_property
    def target_model(self):
        from organisation.models import Person

        return Person

    @cached_property
    def widget(self):
        from organisation.widgets import PersonChooser

        return PersonChooser()

    def get_form_state(self, value):
        return self.widget.get_value_data(value)
