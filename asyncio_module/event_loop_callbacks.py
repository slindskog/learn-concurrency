import time
import random
import asyncio
from asyncio import Future
from threading import Thread, current_thread


def resolver(future):
    print(f"Is loop running in thread: {current_thread().getName()} = {asyncio.get_event_loop().is_running()}")
    time.sleep(2)
    future.set_result(None)


async def coro():
    future = Future()

    loop = asyncio.get_event_loop()
    loop.call_later(5, resolver, future)

    print(f"Is loop running in thread: {current_thread().getName()} = {asyncio.get_event_loop().is_running()}")

    await future
    print("Coro exiting")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(f"Is loop running in thread: {current_thread().getName()} = {asyncio.get_event_loop().is_running()}")
    loop.run_until_complete(coro())
    print("Main exiting")
