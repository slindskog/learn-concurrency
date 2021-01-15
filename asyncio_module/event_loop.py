import time
import asyncio


async def do_something_important():
    await asyncio.sleep(10)


if __name__ == '__main__':
    start = time.time()

    asyncio.run(do_something_important())

    # Python 3.5 syntax
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(do_something_important())

    print(f"Program ran for {time.time() - start} seconds")
