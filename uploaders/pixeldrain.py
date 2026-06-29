import aiohttp
import os

from aiohttp import MultipartWriter

from config import PIXELDRAIN_API_KEY
from utils.upload_stream import UploadStream


async def upload_to_pixeldrain(file_path):

    auth = aiohttp.BasicAuth(
        login="",
        password=PIXELDRAIN_API_KEY
    )

    stream = UploadStream(
        file_path,
        status_message,
        task_id,
        keyboard
    )

    writer = MultipartWriter("form-data")

    part = writer.append(stream)

    part.set_content_disposition(
        "form-data",
        name="file",
        filename=os.path.basename(file_path)
    )

    part.headers["Content-Type"] = "application/octet-stream"

    try:

        async with aiohttp.ClientSession(
            auth=auth
        ) as session:

            async with session.post(
                "https://pixeldrain.com/api/file",
                data=writer
            ) as response:

                text = await response.text()

                if response.status not in (200, 201):
                    raise Exception(
                        f"PixelDrain Error {response.status}\n{text}"
                    )

                data = await response.json()

    finally:

        stream.close()

    if not data.get("success", True):
        raise Exception(
            data.get(
                "message",
                "Upload failed"
            )
        )

    return f"https://pixeldrain.com/u/{data['id']}"
