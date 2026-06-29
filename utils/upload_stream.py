import asyncio
import os

from core.tasks import is_cancelled
from utils.progress import progress


class UploadStream:

    def __init__(
        self,
        file_path,
        status_message,
        task_id,
        keyboard,
        chunk_size=1024 * 256,
    ):

        self.file = open(file_path, "rb")

        self.file_path = file_path

        self.status_message = status_message

        self.task_id = task_id

        self.keyboard = keyboard

        self.chunk_size = chunk_size

        self.total = os.path.getsize(file_path)

        self.current = 0

    async def read(self, size=-1):

        if is_cancelled(self.task_id):
            raise asyncio.CancelledError()

        chunk = self.file.read(
            self.chunk_size
            if size == -1
            else min(size, self.chunk_size)
        )

        if not chunk:
            return b""

        self.current += len(chunk)

        await progress(
            self.current,
            self.total,
            self.status_message,
            "⬆️ Uploading...",
            self.keyboard
        )

        return chunk

    def close(self):
        self.file.close()

    def __len__(self):
        return self.total
