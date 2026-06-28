import os
from urllib.parse import urlparse, unquote

import aiofiles
import httpx

from config import DOWNLOAD_PATH


async def download_direct_file(url: str, status_message=None):
    """
    Download a file from a direct URL and return the local file path.
    """

    if status_message:
        await status_message.edit_text("⬇️ Downloading file...")

    async with httpx.AsyncClient(follow_redirects=True, timeout=None) as client:
        response = await client.get(url)

        response.raise_for_status()

        # Try to get filename from Content-Disposition
        filename = None

        content_disposition = response.headers.get("Content-Disposition")

        if content_disposition and "filename=" in content_disposition:
            filename = content_disposition.split("filename=")[-1].strip('"')

        # Otherwise use filename from URL
        if not filename:
            filename = os.path.basename(
                unquote(urlparse(str(response.url)).path)
            )

        # Final fallback
        if not filename:
            filename = "downloaded_file"

        file_path = os.path.join(DOWNLOAD_PATH, filename)

        async with aiofiles.open(file_path, "wb") as f:
            await f.write(response.content)

    return file_path