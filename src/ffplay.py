import os
from pathlib import Path

from aiomultiprocess import Pool as AsyncPool
from multiprocessing import Pool as SyncPool


class FFplay:

    def __init__(self, ffplay_path: str = os.getenv("FFPLAY_PATH")) -> None:
        self._ffplay_path: Path = Path(ffplay_path)
        if not self._ffplay_path.exists():
            raise FileNotFoundError("FFprobe binary not found!")

    def run(self, *queries: tuple[str], run_async: bool = False, **runner_options) -> None:
        pass
