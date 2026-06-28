import os
import aiofiles


class ProgressFile:
    def __init__(self, file_path, callback):
        self.file_path = file_path
        self.callback = callback

        self.size = os.path.getsize(file_path)
        self.current = 0

    async def __aiter__(self):
        async with aiofiles.open(self.file_path, "rb") as f:

            while True:
                chunk = await f.read(1024 * 256)

                if not chunk:
                    break

                self.current += len(chunk)

                if self.callback:
                    await self.callback(
                        self.current,
                        self.size
                    )

                yield chunk