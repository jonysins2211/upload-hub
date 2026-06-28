import os

import httpx


async def upload_to_pixeldrain(file_path: str):
    """
    Upload a file anonymously to PixelDrain.
    Returns the public download URL.
    """

    filename = os.path.basename(file_path)

    upload_url = f"https://pixeldrain.com/api/file/{filename}"

    async with httpx.AsyncClient(timeout=None) as client:
        with open(file_path, "rb") as file:
            response = await client.put(
                upload_url,
                content=file
            )

    response.raise_for_status()

    data = response.json()

    if not data.get("success"):
        raise Exception(data.get("message", "Upload failed"))

    file_id = data["id"]

    return f"https://pixeldrain.com/u/{file_id}"