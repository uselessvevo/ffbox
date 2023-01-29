import os
import asyncio
from pathlib import Path

from aiomultiprocess import Pool as AsyncPool
from multiprocessing import Pool as SyncPool


class FFmpeg:

    def __init__(
        self, 
        ffmpeg_path: str = os.getenv("FFMPEG_PATH")
    ) -> None:
        self._ffmpeg_path: Path = Path(ffmpeg_path)
        if not self._ffmpeg_path.exists():
            raise FileNotFoundError("FFmpeg binary not found!")

    def run(
        self, 
        *queries: tuple[str],
        run_async: bool = False,
        stdout: bool = False,
        stderr: bool = False,
        **runner_options
    ) -> None:
        if run_async:
            self._run_async(*queries, **runner_options)
            runner = AsyncRunner(*queries, **runner_options)
            runner.run()
        else:
            runner = SyncRunner(*queries, **runner_options)
            runner.run()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (id: {id(self)})"


class SyncRunner:
    
    def __init__(
        self,
        *queries: tuples[str],
        max_processes: int = 2,
    ) -> None:
        pass

    def run(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (id: {id(self)})"


class AsyncRunner:
    
    def __init__(
        self, 
        *queries: tuples[str],
        max_processes: int = 2,
        max_tasks_per_child: int = 0,
        tasks_count: int = None,
        scheduler: "Scheduler" = aiomultiprocess.RoundRobin,
        event_loop: asyncio.AbstractEventLoop = asyncio.new_event_loop,
    ) -> None:
        pass

    def run(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (id: {id(self)})"
