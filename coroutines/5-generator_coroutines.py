import time
from typing import Generator, Any, List, Iterable

NoResult = object()


## Building coroutines from generators

def sleep(duration: float):
    now = time.time()
    delay = now + duration
    while now < delay:
        yield 3
        now = time.time()


def bar():
    yield from sleep(5)
    return 123


def foo():
    value = yield from bar()
    return value


def wait(tasks: Iterable[Generator]) -> List[Any]:
    """
    Instead of calling run() on each task we calling send() on each generator object.
    Rather than looking for a flag we catch stop iteration error and mark those tasks(gens)
    as completed.
    StopIteration by itself contains the return value from these generators. So we save
    those for final result.
    We also capture intermediate yielded values and send them back on the next iteration.
    It enables coroutines call other coroutines - we can now yield from another coroutine
    to call into it and the position in a stack of coroutine calls will be preserved
    across yield
    """
    pending = list(tasks)
    tasks = {task: None for task in pending}
    before = time.time()

    while pending:
        for gen in pending:
            try:
                tasks[gen] = gen.send(tasks[gen])
            except StopIteration as e:
                tasks[gen] = e.args[0]
                pending.remove(gen)

    print(f"duration = {time.time() - before:.3}")
    return list(tasks.values())


def main():
    """
    at each yield event loop is cycling to next pending task - we get cooperative
    multitasking cncurrenrlo6cy
    """
    tasks = [foo(), foo()]
    print(wait(tasks))


if __name__ == "__main__":
    main()
