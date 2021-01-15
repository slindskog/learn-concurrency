import asyncio


# async def -> native coroutine
async def coro():
    # await is used to obtain the result of a coroutine object's execution
    await asyncio.sleep(1)


if __name__ == '__main__':
    # Run the coroutine
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coro())
