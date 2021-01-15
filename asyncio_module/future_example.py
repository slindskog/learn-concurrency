import asyncio
from asyncio import Future


async def bar(future):
    print("Bar will sleep for 3 seconds")
    await asyncio.sleep(3)
    print("Bar resolving the future")
    future.done()
    future.set_result("Future is resolved")


async def foo(future):
    print("Foo will await the future")
    await future
    print("Foo finds the future resolved")


async def main():
    future = Future()
    results = await asyncio.gather(foo(future), bar(future))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("Main exiting")

    # Newer Python 3.7 syntax
    asyncio.run(main())
    print("Main exiting")
