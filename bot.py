from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "UploaderBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "handlers"}
)


if __name__ == "__main__":
    print("🚀 Starting Uploader Bot...")
    app.start()
    print("✅ Bot is running!")
    idle()
    app.stop()
    print("🛑 Bot stopped.")