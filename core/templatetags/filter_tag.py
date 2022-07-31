from django import template

register = template.Library()


@register.filter
def filter_organisation(self, value):
    result = []
    for element in self:
        if element.person.organisation == value:
            result.append(element)
    return result


@register.filter(name="lookup")
def lookup(value, arg):
    return value[arg]
