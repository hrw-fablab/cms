from dotenv import load_dotenv

load_dotenv()
import os

from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

from core.models import FablabImage

from wagtail.core.models import Collection
from django.core.files.images import ImageFile
import json

import tempfile


def get_collection():
    try:
        Collection.objects.get(name="devices")
    except:
        root_coll = Collection.get_first_root_node()
        root_coll.add_child(name="devices")
    finally:
        return Collection.objects.get(name="devices")


def get_image(data):
    try:
        image = json.loads(data["DevicePhoto"])
        return image["fileName"]
    except:
        return False


def enhance_data(data):
    result = []
    for element in data:
        item = element.to_json()
        result.append(
            {
                "title": item["AssetType"] or False,
                "model": item["Model"] or False,
                "area": item["Bereich"] or False,
                "manufacturer": item["Manufacturer"] or False,
                "image": get_image(item),
            }
        )
    return result


def load_data():
    site_url = "https://hrwfablab.sharepoint.com/sites/HRWFablab"
    ctx = ClientContext(site_url).with_credentials(
        UserCredential(
            os.environ.get("SHAREPOINT_EMAIL"), os.environ.get("SHAREPOINT_PASSWORD")
        )
    )

    collection = get_collection()
    target_list = ctx.web.lists.get_by_title("Inventurliste").get().execute_query()
    items = target_list.items.get().execute_query()

    enhanced_items = enhance_data(items)

    for item in enhanced_items:
        if item["image"] == False:
            continue

        file_url = (
            "/sites/HRWFablab/SiteAssets/Lists/557ea859-2788-41e5-abc9-fc01112bf884/"
            + item["image"]
        )
        FablabImage.objects.all().filter(title=item["image"]).delete()

        with tempfile.TemporaryFile() as local_file:
            ctx.web.get_file_by_server_relative_path(file_url).download(
                local_file
            ).execute_query()

            image_file = ImageFile(local_file, name=item["image"])
            image = FablabImage(
                title=item["image"], file=image_file, collection=collection
            )
            image.save()

    return enhanced_items
