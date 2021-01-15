import asyncio


async def coro3(k):
    return k + 3


async def coro2(j):
    j *= j
    result = await coro3(j)
    return result


async def coro1():
    i = 0
    while i < 100:
        final_result = await coro2(i)
        print(f"({i}) = {final_result}")
        i += 1


if __name__ == '__main__':
    # The 1st 100 natural numbers evaluated for x^2 + 3
    cr = coro1()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cr)
