from pyrogram import Client, idle
from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    BOT_WORKERS,
    MAX_CONCURRENT_TRANSMISSIONS,
)

app = Client(
    "UploaderBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "handlers"},
    workers=BOT_WORKERS,
    max_concurrent_transmissions=MAX_CONCURRENT_TRANSMISSIONS,
)


if __name__ == "__main__":
    print("🚀 Starting Uploader Bot...")
    app.start()
    print("✅ Bot is running!")
    idle()
    app.stop()
    print("🛑 Bot stopped.")