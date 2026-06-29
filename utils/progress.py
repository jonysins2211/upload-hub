import time

_last = {}


def human_size(size):
    if size is None:
        return "Unknown"

    size = float(size)

    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def human_time(seconds):
    if seconds <= 0:
        return "--:--"

    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)

    if hours:
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    return f"{minutes:02}:{seconds:02}"


async def progress(
    current,
    total,
    message,
    action,
    keyboard=None
):

    key = f"{message.chat.id}:{message.id}"
    now = time.time()

    if key not in _last:
        _last[key] = {
            "time": now,
            "bytes": current,
            "last_edit": 0
        }

    data = _last[key]

    # Edit every 5 seconds
    if current != total and now - data["last_edit"] < 5:
        return

    elapsed = now - data["time"]

    transferred = current - data["bytes"]

    speed = transferred / elapsed if elapsed > 0 else 0

    eta = (
        (total - current) / speed
        if speed > 0 and total
        else 0
    )

    data["time"] = now
    data["bytes"] = current
    data["last_edit"] = now

    if total:

        percent = current * 100 / total

        filled = int(percent / 5)

        bar = (
            "█" * filled +
            "░" * (20 - filled)
        )

        text = (
            f"{action}\n\n"
            f"`{bar}` {percent:.2f}%\n\n"
            f"📦 {human_size(current)} / {human_size(total)}\n"
            f"⚡ {human_size(speed)}/s\n"
            f"⏳ ETA: {human_time(eta)}"
        )

    else:

        text = (
            f"{action}\n\n"
            f"📦 Downloaded: {human_size(current)}\n"
            f"⚡ {human_size(speed)}/s"
        )

    try:
        await message.edit_text(
            text,
            reply_markup=keyboard
        )
    except:
        pass

    if current == total:
        _last.pop(key, None)
