import time
import asyncio
from asyncio import Future
from threading import current_thread

shutdown = False


async def resolver(future):
    print(f"Is loop running in thread: {current_thread().getName()} = {asyncio.get_event_loop().is_running()}")

    await asyncio.sleep(10)

    future.set_result(None)


async def monitor_coro():
    global shutdown

    while shutdown == False:
        print(f"Alive at {time.time()}")
        await asyncio.sleep(1)


async def coro():
    global shutdown

    print("Coro running")
    future = Future()

    loop = asyncio.get_event_loop()
    monitor_coro_future = asyncio.ensure_future(monitor_coro())
    resolver_future = asyncio.ensure_future(resolver(future))

    print(f"Is loop running in thread: {current_thread().getName()} = {asyncio.get_event_loop().is_running()}")

    await future
    await asyncio.sleep(2)

    shutdown = True

    await monitor_coro_future, resolver_future
    print("Coro exiting")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(f"Is loop running in thread: {current_thread().getName()} = {asyncio.get_event_loop().is_running()}")
    loop.run_until_complete(coro())
    print("Main exiting")
