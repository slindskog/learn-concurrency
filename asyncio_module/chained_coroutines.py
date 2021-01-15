import asyncio
from asyncio import Future


# Chain wouldn't run with asyncio's event loop since
# it does not work with generators.
# def coro3(k):
#    yield (k + 3)


def coro3(k):
    f = Future()
    f.set_result(k + 3)
    f.done()
    return f


def coro2(j):
    j *= j
    result = yield from coro3(j)
    return result


def coro1():
    i = 0
    while i < 100:
        final_result = yield from coro2(i)
        print(f"({i}) = {final_result}")
        yield from coro2(i)
        i += 1


if __name__ == '__main__':
    # The 1st 100 natural numbers evaluated for x^2 + 3
    cr = coro1()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cr)
