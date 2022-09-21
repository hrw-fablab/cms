from dotenv import load_dotenv

load_dotenv()
import os

from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext


def load_data():
    site_url = "https://hrwfablab.sharepoint.com/sites/HRWFablab"
    ctx = ClientContext(site_url).with_credentials(
        UserCredential(
            os.environ.get("SHAREPOINT_EMAIL"), os.environ.get("SHAREPOINT_PASSWORD")
        )
    )
    target_list = ctx.web.lists.get_by_title("Inventurliste").get().execute_query()
    result = []
    items = target_list.items.get().execute_query()
    for item in items:
        print(item.properties)
        result.append(
            {
                "title": item.properties["AssetType"],
                "model": item.properties["Model"],
                "area": item.properties["Bereich"],
                "manufacturer": item.properties["Manufacturer"],
            }
        )
    return result
