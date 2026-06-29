import os
import aiohttp

from aiohttp import MultipartWriter

from config import GOFILE_API_TOKEN
from utils.upload_stream import UploadStream


async def upload_to_gofile(
    file_path,
    status_message,
    task_id,
    keyboard
):

    headers = {
        "Authorization": f"Bearer {GOFILE_API_TOKEN}"
    }

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
            headers=headers
        ) as session:

            async with session.post(
                "https://upload.gofile.io/uploadfile",
                data=writer
            ) as response:

                text = await response.text()

                try:
                    data = await response.json(content_type=None)
                except Exception:
                    raise Exception(
                        f"HTTP {response.status}\n\n{text}"
                    )

                if response.status not in (200, 201):
                    raise Exception(
                        data.get(
                            "message",
                            f"HTTP {response.status}"
                        )
                    )

    finally:

        stream.close()

    if data.get("status") != "ok":
        raise Exception(
            data.get(
                "message",
                "Upload failed"
            )
        )

    return data["data"]["downloadPage"]
