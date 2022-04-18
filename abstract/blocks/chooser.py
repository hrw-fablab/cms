from wagtail.core import blocks


class ProjectChooserBlock(blocks.ChooserBlock):
    @property
    def target_model(self):
        from organisation.models import Project

        return Project

    @property
    def widget(self):
        from chooser.widgets import ProjectChooser

        return ProjectChooser()

    def get_form_state(self, value):
        return self.widget.get_value_data(value)


class PersonChooserBlock(blocks.ChooserBlock):
    @property
    def target_model(self):
        from organisation.models import Person

        return Person

    @property
    def widget(self):
        from chooser.widgets import PersonChooser

        return PersonChooser()

    def get_form_state(self, value):
        return self.widget.get_value_data(value)
