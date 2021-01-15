import time
import asyncio
import inspect
from threading import Thread


@asyncio.coroutine
def sleeping_generator():
    time.sleep(3)
    yield None


def run_generator(gen):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    next(gen)


if __name__ == '__main__':
    gen = sleeping_generator()
    Thread(target=run_generator, args=(gen,)).start()

    i = 0
    while i != 5:
        print(f"Generator state: {inspect.getgeneratorstate(gen)}")
        time.sleep(0.1)
        i += 1
