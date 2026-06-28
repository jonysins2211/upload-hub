from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    await message.reply_text(
        "👋 Welcome!\n\n"
        "Send me:\n"
        "• A Telegram file\n"
        "• A direct download link\n\n"
        "I'll ask where you want to upload it."
    )