import time
import asyncio
from asyncio import Future
from threading import Thread, current_thread


async def asleep(sleep_for):
    future = Future()
    current_loop = asyncio.get_event_loop()
    Thread(target=sync_sleep, args=(sleep_for, future, current_loop)).start()
    await future


def sync_sleep(sleep_for, future, loop):
    # Sleep synchronously
    time.sleep(sleep_for)

    # Define a nested coroutine to resolve the future
    async def sleep_future_resolver():
        # Resolve the future
        future.set_result(None)

    asyncio.run_coroutine_threadsafe(sleep_future_resolver(), loop)
    print(f"Sleeping completed in {current_thread().getName()}s\n", flush=True)


if __name__ == '__main__':
    start = time.time()
    work = []
    for _ in range(5):
        work.append(asleep(5))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(work, return_when=asyncio.ALL_COMPLETED))
    print(f"Main program exiting after running for {time.time() - start}")
