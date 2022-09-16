from django import template

register = template.Library()

from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext


def reduce_item(item):
    return {"title": item.Title}


def query_large_list(target_list):
    """
    :type target_list: office365.sharepoint.lists.list.List
    """
    paged_items = target_list.items.get().execute_query()
    print(paged_items)
    # all_items = [item for item in paged_items]
    # print("Total items count: {0}".format(len(all_items)))


@register.simple_tag
def get_devices():
    site_url = "https://hrwfablab.sharepoint.com/sites/HRWFablab"
    ctx = ClientContext(site_url).with_credentials(UserCredential("xxx", "xxxx"))
    target_list = ctx.web.lists.get_by_title("Inventurliste").get().execute_query()
    return target_list.items.get().execute_query()
