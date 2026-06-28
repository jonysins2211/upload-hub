import os
import aiohttp


async def upload_to_pixeldrain(file_path: str):
    """
    Upload a file anonymously to PixelDrain.
    Returns the public URL.
    """

    url = "https://pixeldrain.com/api/file"

    form = aiohttp.FormData()

    with open(file_path, "rb") as f:
        form.add_field(
            "file",
            f,
            filename=os.path.basename(file_path),
            content_type="application/octet-stream"
        )

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=form) as response:

                text = await response.text()

                if response.status != 200:
                    raise Exception(
                        f"PixelDrain Error {response.status}: {text}"
                    )

                data = await response.json()

    return f"https://pixeldrain.com/u/{data['id']}"