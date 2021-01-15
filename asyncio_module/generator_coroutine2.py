import time
import asyncio
from threading import current_thread


@asyncio.coroutine
def go_to_sleep(sleep):
    print(f"Sleeping for {sleep} seconds in thread {current_thread().getName()}")
    yield from asyncio.sleep(sleep)
    # This will become serially executed with time.sleep
    # time.sleep(sleep)


@asyncio.coroutine
def do_something_important(sleep):
    yield from go_to_sleep(sleep)


if __name__ == '__main__':
    now = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(do_something_important(1), do_something_important(2), do_something_important(3))
    )
    end = time.time()
    print(f"Total time to run: {end - now}")
    loop.close()
