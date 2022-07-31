from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag(name='form_field_attribute')
def form_field_attribute(form_page, field, attribute_name, default=None):
    """Return attribute on FormField where field matches 'field' provided."""
    # field is a django Field instance
    field_name = field.name
    results = [
        # if html is stored, need to use mark_safe - be careful though.
        mark_safe(getattr(form_field, attribute_name, default))
        # get_form_fields() is a built in function on AbstractFormPage
        for form_field in form_page.get_form_fields()
        # clean_name is property on AbstractFormField used for Django Field name
        if form_field.clean_name == field_name]
    if results:
        return results[0]
    return default
