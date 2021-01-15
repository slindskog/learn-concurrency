import asyncio


# @asyncio.coroutine to be removed in Python 3.10
@asyncio.coroutine
def gen_based_coro():
    return 10


async def main():
    rcvd = await gen_based_coro()
    print(f"native coroutine received: {rcvd}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
