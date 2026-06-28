import os
import aiohttp


async def upload_to_gofile(file_path: str):
    """
    Upload a file anonymously to GoFile.
    Returns the public download URL.
    """

    # Step 1: Get an upload server
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://api.gofile.io/getServer"
        ) as response:

            if response.status != 200:
                raise Exception("Unable to get GoFile upload server.")

            data = await response.json()

            server = (
                data.get("data", {}).get("server")
                or data.get("server")
            )

            if not server:
                raise Exception("GoFile server not found.")

    upload_url = f"https://{server}.gofile.io/uploadFile"

    form = aiohttp.FormData()

    with open(file_path, "rb") as file:
        form.add_field(
            "file",
            file,
            filename=os.path.basename(file_path),
            content_type="application/octet-stream",
        )

        async with aiohttp.ClientSession() as session:
            async with session.post(
                upload_url,
                data=form
            ) as response:

                if response.status not in (200, 201):
                    raise Exception(await response.text())

                result = await response.json(content_type=None)

    if result.get("status") != "ok":
        raise Exception(result)

    return result["data"]["downloadPage"]