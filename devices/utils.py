from dotenv import load_dotenv

load_dotenv()
import os

from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

from core.models import FablabImage

from wagtail.images.models import Image
from wagtail.core.models import Collection
from django.core.files.images import ImageFile
import json

import os
import tempfile

c_id = Collection.objects.get(name="HRW FabLab")


def load_data():
    site_url = "https://hrwfablab.sharepoint.com/sites/HRWFablab"
    ctx = ClientContext(site_url).with_credentials(
        UserCredential(
            os.environ.get("SHAREPOINT_EMAIL"), os.environ.get("SHAREPOINT_PASSWORD")
        )
    )

    download_folder = tempfile.mkdtemp()

    target_list = ctx.web.lists.get_by_title("Inventurliste").get().execute_query()
    result = []
    items = target_list.items.get().execute_query()
    for item in items:
        try:
            json_item = item.to_json()
            result.append(
                {
                    "title": json_item["AssetType"] or False,
                    "model": json_item["Model"] or False,
                    "area": json_item["Bereich"] or False,
                    "manufacturer": json_item["Manufacturer"] or False,
                }
            )
        except:
            continue

        try:
            file = json.loads(json_item["DevicePhoto"])
            file_url = (
                "/sites/HRWFablab/SiteAssets/Lists/557ea859-2788-41e5-abc9-fc01112bf884/"
                + file["fileName"]
            )
        except:
            continue

        download_path = os.path.join(download_folder, os.path.basename(file_url))
        with open(download_path, "wb") as local_file:
            title = file["fileName"]
            ctx.web.get_file_by_server_relative_path(file_url).download(
                local_file
            ).execute_query()
            image_file = ImageFile(open(download_path, "rb"), name=title)
            image = FablabImage(title=title, file=image_file, collection=c_id)
            image.save()

    return result
