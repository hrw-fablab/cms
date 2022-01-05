from django import template
from ..models import Author, DeviceCategory, ProjectCategory, Tag

register = template.Library()

@register.inclusion_tag('', takes_context=True)
def authors(context):
	return {
		'authors': Author.objects.all(),
		'request': context['request'],
	}

@register.inclusion_tag('', takes_context=True)
def tags(context):
	return {
		'tags': Tag.objects.all(),
		'request': context['request'],
	}

@register.inclusion_tag('', takes_context=True)
def devicecategorys(context):
	return {
		'DeviceCategorys': DeviceCategory.objects.all(),
		'request': context['request'],
	}

@register.inclusion_tag('', takes_context=True)
def projectcategorys(context):
	return {
		'ProjectCategorys': ProjectCategory.objects.all(),
		'request': context['request'],
	}