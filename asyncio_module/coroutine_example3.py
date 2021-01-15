import asyncio


# Generator-based coroutine using yield-from to await native coroutine asyncio.sleep()
@asyncio.coroutine
def gen_based_coro():
    yield from asyncio.sleep(1)


if __name__ == '__main__':
    gen = gen_based_coro()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gen)
