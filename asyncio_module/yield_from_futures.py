import asyncio
from asyncio import Future


def yield_from_task_example():
    # Create a task to sleep for 5 seconds
    task = asyncio.get_event_loop().create_task(asyncio.sleep(5))
    yield from task


if __name__ == '__main__':
    f = Future()

    # Future has an __iter__() method
    it = f.__iter__()
    print(next(it))

    # Set the future's result and mark it done
    f.set_result("hello")
    f.done()

    try:
        next(it)
    except StopIteration as si:
        print(si.value)

    # Yield from task
    loop = asyncio.get_event_loop()
    loop.run_until_complete(yield_from_task_example())
