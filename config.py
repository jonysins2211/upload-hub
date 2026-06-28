import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Directories
DOWNLOAD_PATH = "downloads"

# Automatically create downloads directory
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

# Optional limits
MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024  # 2 GB