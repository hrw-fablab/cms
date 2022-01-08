from django import template
from wagtail.core.models import Site

register = template.Library()

@register.simple_tag(takes_context=True)
def get_site_root(context):
	return Site.find_for_request(context['request']).root_page


def is_active(page, current_page):
	return (current_page.url_path.startswith(page.url_path) if current_page else False)


# Retrieves the top menu items
@register.inclusion_tag('cms/templatetags/footer_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
	menuitems = parent.get_children().live().in_menu()

	for menuitem in menuitems:
		# We don't directly check if calling_page is None since the template
		# engine can pass an empty string to calling_page
		# if the variable passed as calling_page does not exist.
		menuitem.active = (calling_page.url_path.startswith(menuitem.url_path)
						   if calling_page else False)
	return {
		'calling_page': calling_page,
		'menuitems': menuitems,
		# required by the pageurl tag that we want to use within this template
		'request': context['request'],
	}