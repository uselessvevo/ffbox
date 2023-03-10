import os
from pathlib import Path

from aiomultiprocess import Pool as AsyncPool
from multiprocessing import Pool as SyncPool


class FFprobe:

    def __init__(self, ffprobe_path: str = os.getenv("FFPROBE_PATH")) -> None:
        self._ffprobe_path: Path = Path(ffprobe_path)
        if not self._ffprobe_path.exists():
            raise FileNotFoundError("FFprobe binary not found!")

    def run(self, *queries: tuple[str], run_async: bool = False, **runner_options) -> None:
        pass
