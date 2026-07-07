import os

from pyrogram.types import Message

from config import DOWNLOAD_PATH
from utils.progress import progress

async def download_telegram_file(
    message: Message,
    status_message=None,
    task_id=None,
    keyboard=None
):
    """
    Downloads a Telegram file and returns its local path.
    """

    media = (
        message.document
        or message.video
        or message.audio
        or message.photo
        or message.animation
        or message.voice
    )

    if not media:
        raise ValueError("No downloadable media found, send Telegram file or a direct download link.")

    filename = getattr(media, "file_name", None)

    if not filename:
        filename = f"{media.file_unique_id}.bin"

    task_download_path = os.path.join(DOWNLOAD_PATH, task_id or str(message.id))
    os.makedirs(task_download_path, exist_ok=True)

    file_path = os.path.join(task_download_path, filename)

    if status_message:
        await status_message.edit_text(
            "⬇️ Downloading file...",
            reply_markup=keyboard
        )


    await message.download(
        file_name=file_path,
        progress=progress,
        progress_args=(
            status_message,
            "⬇️ Downloading...",
            keyboard
        )
    )
    
    return file_path
