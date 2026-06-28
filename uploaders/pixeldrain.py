import os
import aiohttp


async def upload_to_pixeldrain(file_path: str):
    """
    Upload a file anonymously to PixelDrain.
    Returns the public download URL.
    """

    filename = os.path.basename(file_path)

    url = f"https://pixeldrain.com/api/file/{filename}"

    async with aiohttp.ClientSession() as session:
        with open(file_path, "rb") as file:

            async with session.put(
                url,
                data=file
            ) as response:

                response.raise_for_status()

                result = await response.json()

    if not result.get("success"):
        raise Exception(result.get("message", "Upload failed"))

    return f"https://pixeldrain.com/u/{result['id']}"