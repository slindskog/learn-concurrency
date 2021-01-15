import types
import asyncio
import inspect


# Coroutine function
@asyncio.coroutine
def hello_world():
    print("Hello world!")


# Uncomment to make awaitable
# @asyncio.coroutine
def silly():
    item = yield None
    print(item)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(hello_world())

    s = silly()
    print(inspect.isawaitable(s))
    print(isinstance(s, types.GeneratorType))
