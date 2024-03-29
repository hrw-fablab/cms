import os
import json
import tempfile

from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from cms.core.models import FablabImage
from wagtail.models import Collection
from django.core.files.images import ImageFile
from dotenv import load_dotenv

from .models import Device


load_dotenv()


def link_image(item):
    if not item:
        return None
    return FablabImage.objects.filter(title=item).first()


def create_devices(data):
    devices = []
    for item in data:
        devices.append(
            Device(
                title=item["title"],
                model=item["model"],
                area=item["area"],
                manufacturer=item["manufacturer"],
                amount=item["amount"],
                image=link_image(item["image"]),
            )
        )
    return devices


def get_index(data, model):
    for i, item in enumerate(data):
        if item["model"] == model:
            return i


def get_collection():
    try:
        Collection.objects.get(name="devices")
    except:  # noqa
        root_coll = Collection.get_first_root_node()
        root_coll.add_child(name="devices")
    finally:
        return Collection.objects.get(name="devices")


def load_data():
    site_url = "https://hrwfablab.sharepoint.com/sites/HRWFablab"
    ctx = ClientContext(site_url).with_credentials(
        UserCredential(
            os.environ.get("SHAREPOINT_EMAIL"), os.environ.get("SHAREPOINT_PASSWORD")
        )
    )

    target_list = ctx.web.lists.get_by_title("Inventurliste")
    items = target_list.items.get_all().execute_query()

    return items


def enhance_image(data):
    try:
        image = json.loads(data["DevicePhoto"])
        return image["fileName"]
    except:  # noqa
        return False


def enhance_data(data):
    result = []
    for element in data:
        item = element.to_json()
        if item["Webseite"] is None:
            continue
        result.append(
            {
                "title": item["AssetType"] or False,
                "model": item["Model"] or False,
                "area": item["Bereich"] or False,
                "manufacturer": item["Manufacturer"] or False,
                "image": enhance_image(item),
            }
        )
    return result


def reduce_data(data):
    reduced = []
    models = []
    for item in data:
        item["amount"] = 1
        model = item["model"]

        if model in models:
            index = get_index(reduced, model)
            reduced[index]["amount"] += 1
            continue

        models.append(model)
        reduced.append(item)

    return reduced


def load_images(data):
    site_url = "https://hrwfablab.sharepoint.com/sites/HRWFablab"
    ctx = ClientContext(site_url).with_credentials(
        UserCredential(
            os.environ.get("SHAREPOINT_EMAIL"), os.environ.get("SHAREPOINT_PASSWORD")
        )
    )

    collection = get_collection()

    for item in data:
        if item["image"] is False:
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
