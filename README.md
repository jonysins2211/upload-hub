# 🚀 UploadHub
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Pyrogram](https://img.shields.io/badge/Pyrogram-2.x-blue)
![License](https://img.shields.io/github/license/subashbuilds/UploadHub)
![Stars](https://img.shields.io/github/stars/subashbuilds/UploadHub?style=social)
![Forks](https://img.shields.io/github/forks/subashbuilds/UploadHub?style=social)
![Issues](https://img.shields.io/github/issues/subashbuilds/UploadHub)
![Last Commit](https://img.shields.io/github/last-commit/subashbuilds/UploadHub)
A powerful and lightweight Telegram bot built with **Pyrogram** that downloads files from **Telegram** or **direct download links** and uploads them to **PixelDrain** or **GoFile**.

---

## ✨ Features

- 📂 Upload Telegram media files
- 🌐 Upload files from direct download links
- ☁️ Upload to **PixelDrain**
- 📦 Upload to **GoFile**
- 📊 Real-time download progress
  - Percentage
  - Speed
  - ETA
  - Progress bar
- 📄 Automatic filename detection
- 📏 Automatic file size detection
- 🗑️ Automatic cleanup after upload
- 🔄 `/update` command for GitHub auto-update (Sudo users only)
- 👮 Sudo user management
- ⚡ Async architecture using Pyrogram

---

## 📸 Workflow

```text
Telegram File / Direct Link
           │
           ▼
   Select Upload Destination
           │
   ┌───────┴────────┐
   │                │
PixelDrain      GoFile
   │                │
   ▼                ▼
 Upload Complete → Download Link
```

---

# 🛠️ Requirements

- Python 3.10+
- Telegram Bot Token
- Telegram API ID & API Hash
- PixelDrain API Key (Optional)
- GoFile API Token (Optional)

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/UploadHub.git

cd UploadHub
```

Create a virtual environment

```bash
python3 -m venv venv
```

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuration

Create a `.env` file.

```env
API_ID=
API_HASH=
BOT_TOKEN=

PIXELDRAIN_API_KEY=
GOFILE_API_TOKEN=

SUDO_USERS=123456789
```

---

# ▶️ Running

```bash
python3 -m bot
```

---

# 📂 Project Structure

```text
UploadHub/
│
├── bot.py
├── config.py
├── requirements.txt
├── .env
│
├── handlers/
│   ├── messages.py
│   ├── callbacks.py
│   └── update.py
│
├── downloaders/
│   ├── telegram.py
│   └── direct.py
│
├── uploaders/
│   ├── pixeldrain.py
│   └── gofile.py
│
├── core/
│   └── tasks.py
│
├── utils/
│   ├── helpers.py
│   ├── progress.py
│   └── url_info.py
│
└── downloads/
```

---

# 📊 Download Progress

The bot displays real-time download progress.

```text
⬇️ Downloading...

████████████░░░░░░░░ 63.24%

📦 632 MB / 1.00 GB
⚡ 14.52 MB/s
⏳ ETA: 00:28
```

---

# 📥 Supported Inputs

- Telegram Documents
- Telegram Videos
- Telegram Audio
- Telegram Photos
- Telegram Animations
- Telegram Voice Messages
- Direct Download Links

---

# ☁️ Supported Upload Destinations

- PixelDrain
- GoFile

---

# 🔄 Auto Update

Sudo users can update the bot directly from Telegram.

```
/update
```

The bot will:

- Pull the latest changes from GitHub
- Install new dependencies
- Restart automatically

---

# 🔐 Sudo Users

Only users listed in

```env
SUDO_USERS=
```

can execute administrative commands like `/update`.

---

# ❤️ Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss your ideas.

---

# 🤝 Support

If you encounter any issues or have feature requests, please open an issue on GitHub.

⭐ If you find this project useful, consider giving it a star to support future development.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Subash Krishnan**

GitHub: https://github.com/subashbuilds