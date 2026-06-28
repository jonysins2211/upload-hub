import os
import time


class UploadStream:
    """
    Wraps a file object and reports upload progress every time aiohttp
    reads data from it.
    """

    def __init__(
        self,
        file_path,
        progress_callback=None,
        message=None,
        action="⬆️ Uploading..."
    ):
        self.file = open(file_path, "rb")

        self.size = os.path.getsize(file_path)
        self.current = 0

        self.progress_callback = progress_callback
        self.message = message
        self.action = action

        self.last_update = 0

    def read(self, size=-1):
        data = self.file.read(size)

        if data:
            self.current += len(data)

            now = time.time()

            # Update every 5 seconds or when finished
            if (
                now - self.last_update >= 5
                or self.current >= self.size
            ):
                self.last_update = now

                if self.progress_callback:
                    import asyncio

                    try:
                        loop = asyncio.get_running_loop()

                        loop.create_task(
                            self.progress_callback(
                                self.current,
                                self.size,
                                self.message,
                                self.action
                            )
                        )

                    except RuntimeError:
                        pass

        return data

    def close(self):
        self.file.close()

    # Delegate everything else to the real file object
    def __getattr__(self, item):
        return getattr(self.file, item)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()