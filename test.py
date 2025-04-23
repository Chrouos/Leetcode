from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    MofNCompleteColumn,
    TransferSpeedColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)

class RichProgress:
    def __init__(self, iterable, description="處理中..."):
        self.iterable = iterable
        self.description = description
        self.progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            MofNCompleteColumn(),
            TransferSpeedColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
        )

    def __iter__(self):
        with self.progress as progress:
            task = progress.add_task(f"[cyan]{self.description}", total=len(self.iterable))
            for item in self.iterable:
                yield item
                progress.update(task, advance=1)

from time import sleep

for i in RichProgress(range(1000), description="處理資料中..."):
    # 做你的事
    sleep(0.01)  # 可加可不加
