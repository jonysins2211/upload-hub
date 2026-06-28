import time

_last_update = {}


def human_size(size):
    if size is None:
        return "0 B"

    units = ["B", "KB", "MB", "GB", "TB"]

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


async def progress(current, total, message, action):
    now = time.time()

    chat_id = message.chat.id
    msg_id = message.id
    key = f"{chat_id}:{msg_id}"

    # Update at most once every 2 seconds
    if key in _last_update and now - _last_update[key] < 2:
        return

    _last_update[key] = now

    percent = current * 100 / total if total else 0

    completed = int(percent / 10)
    bar = "█" * completed + "░" * (10 - completed)

    text = (
        f"{action}\n\n"
        f"`{bar}` {percent:.1f}%\n\n"
        f"📦 {human_size(current)} / {human_size(total)}"
    )

    try:
        await message.edit_text(text)
    except Exception:
        pass