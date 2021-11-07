import time
from typing import Iterable, Any


class Task:
    """
    Execute run() until task returns or yields result (ready=True). At that point we can check
    result
    """
    def __init__(self):
        self.ready = False
        self.counter = 0
        self.result = None

    def run(self) -> None:
        raise NotImplemented


class Sleep(Task):
    """
    Execute this task (via run()) until the time has passed so result will be available.
    """
    def __init__(self, duration, result=None):
        super().__init__()
        self.threshold = time.time() + duration
        self.result = result

    def run(self) -> None:
        now = time.time()
        if now >= self.threshold:
            self.ready = True
            print('task completed')


def wait(task: Iterable[Task]) -> list[Any]:
    """
    Create an event loop to run multiple tasks concurrently.
    Each task manually keeps track of its progress and each task has to start from
    the beginning every time
    """
    orig: list[Task] = list(task)
    pending: set[Task] = set(orig)
    before = time.time()
    counter = 0
    while pending:
        for task in list(pending):
            task.run()
            if task.ready:
                pending.remove(task)
                counter += 1
                print(counter)

    print(counter)
    print(f'duration = {time.time() - before}')
    return [task.result for task in orig]


def main():
    tasks = [Sleep(randint(1, 10)) for _ in range(10000)]
    wait(tasks)


main()
