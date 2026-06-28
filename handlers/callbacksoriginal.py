from pyrogram import Client
from pyrogram.types import CallbackQuery
from pyrogram.handlers import CallbackQueryHandler


@Client.on_callback_query()
async def callback_handler(client: Client, callback: CallbackQuery):
    data = callback.data

    if data.startswith("pixeldrain"):
        destination = "PixelDrain"

    elif data.startswith("gofile"):
        destination = "GoFile"

    else:
        await callback.answer("Invalid option!", show_alert=True)
        return

    await callback.answer()

    await callback.message.edit_text(
        f"⏳ Preparing upload to **{destination}**..."
    )