import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

BOT_WORKERS = int(os.getenv("BOT_WORKERS", "16"))
MAX_CONCURRENT_TRANSMISSIONS = int(
    os.getenv("MAX_CONCURRENT_TRANSMISSIONS", "8")
)
DIRECT_DOWNLOAD_CHUNK_SIZE = int(
    os.getenv("DIRECT_DOWNLOAD_CHUNK_SIZE", str(4 * 1024 * 1024))
)

PIXELDRAIN_API_KEY = os.getenv("PIXELDRAIN_API_KEY")
GOFILE_API_TOKEN = os.getenv("GOFILE_API_TOKEN")

SUDO_USERS = [
    int(x)
    for x in os.getenv("SUDO_USERS", "").split(",")
    if x.strip()
]
# Directories
DOWNLOAD_PATH = "downloads"

# Automatically create downloads directory
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

# Optional limits
MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024  # 2 GB