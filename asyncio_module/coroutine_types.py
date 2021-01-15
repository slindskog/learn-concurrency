import asyncio
import types
import inspect
from collections.abc import Iterable, Awaitable


# Ordinary Function
def ordinary_function():
    pass


# Ordinary Function with @asyncio.coroutine decorator
@asyncio.coroutine
def ordinary_function_with_asyncio_coroutine_dec():
    pass


# Ordinary Function with @types.coroutine decorator
@types.coroutine
def ordinary_function_with_types_coroutine_dec():
    pass


# Simple Generator
def simple_generator():
    assign_me = yield 0


# Simple Generator with @asyncio.coroutine decorator
@asyncio.coroutine
def simple_generator_with_asyncio_coroutine_dec():
    assign_me = yield 0


# Simple Generator with @types.coroutine decorator
@types.coroutine
def simple_generator_with_types_coroutine_dec():
    assign_me = yield 0


# Generator-based coroutine
def generator_based_coroutine():
    yield from asyncio.sleep(1)


# Generator-based coroutine with @asyncio.coroutine decorator
@asyncio.coroutine
def generator_based_coroutine_with_asyncio_coroutine_dec():
    yield from asyncio.sleep(1)


# Generator-based coroutine with @types.coroutine decorator
@types.coroutine
def generator_based_coroutine_with_types_coroutine_dec():
    yield from asyncio.sleep(1)


# Native coroutine
async def native_coroutine():
    pass


if __name__ == "__main__":
    of_aio_dec = ordinary_function_with_asyncio_coroutine_dec()
    print(of_aio_dec)
    print("simple generator instance of collections.abc.Iterable : " + str(isinstance(of_aio_dec, Iterable)))
    print("simple generator instance of collections.abc.Awaitable : " + str(isinstance(of_aio_dec, Awaitable)))
    print("simple generator instance of types.Generator : " + str(isinstance(of_aio_dec, types.GeneratorType)))
    print("simple generator instance of types.CoroutineType : " + str(isinstance(of_aio_dec, types.CoroutineType)))
    print("simple generator instance of asyncio.iscoroutine : " + str(asyncio.iscoroutine(of_aio_dec)))
    print("simple generator instance of asyncio.iscoroutinefunction : " + str(
        asyncio.iscoroutinefunction(ordinary_function_with_asyncio_coroutine_dec)))
    print("simple generator instance of inspect.iscoroutine : " + str(inspect.iscoroutine(of_aio_dec)))
    print("generator instance of inspect.iscoroutinefunction : " + str(
        inspect.iscoroutinefunction(ordinary_function_with_asyncio_coroutine_dec)))
    print("simple generator instance of inspect.isawaitable : " + str(inspect.isawaitable(of_aio_dec)))
    print("\n\n")

    of_types_dec = ordinary_function_with_asyncio_coroutine_dec()
    print(of_types_dec)
    print("simple generator instance of collections.abc.Iterable : " + str(isinstance(of_types_dec, Iterable)))
    print("simple generator instance of collections.abc.Awaitable : " + str(isinstance(of_types_dec, Awaitable)))
    print("simple generator instance of types.Generator : " + str(isinstance(of_types_dec, types.GeneratorType)))
    print("simple generator instance of types.CoroutineType : " + str(isinstance(of_types_dec, types.CoroutineType)))
    print("simple generator instance of asyncio.iscoroutine : " + str(asyncio.iscoroutine(of_types_dec)))
    print("simple generator instance of asyncio.iscoroutinefunction : " + str(
        asyncio.iscoroutinefunction(ordinary_function_with_types_coroutine_dec)))
    print("simple generator instance of inspect.iscoroutine : " + str(inspect.iscoroutine(of_types_dec)))
    print("generator instance of inspect.iscoroutinefunction : " + str(
        inspect.iscoroutinefunction(ordinary_function_with_types_coroutine_dec)))
    print("simple generator instance of inspect.isawaitable : " + str(inspect.isawaitable(of_aio_dec)))
    print("\n\n")

    sg = simple_generator()
    print(sg)
    print("simple generator instance of collections.abc.Iterable : " + str(isinstance(sg, Iterable)))
    print("simple generator instance of collections.abc.Awaitable : " + str(isinstance(sg, Awaitable)))
    print("simple generator instance of types.Generator : " + str(isinstance(sg, types.GeneratorType)))
    print("simple generator instance of types.CoroutineType : " + str(isinstance(sg, types.CoroutineType)))
    print("simple generator instance of asyncio.iscoroutine : " + str(asyncio.iscoroutine(sg)))
    print("simple generator instance of asyncio.iscoroutinefunction : " + str(
        asyncio.iscoroutinefunction(simple_generator)))
    print("simple generator instance of inspect.iscoroutine : " + str(inspect.iscoroutine(sg)))
    print("generator instance of inspect.iscoroutinefunction : " + str(
        inspect.iscoroutinefunction(simple_generator)))
    print("simple generator instance of inspect.isawaitable : " + str(inspect.isawaitable(sg)))
    print("\n\n")

    sg_aio_dec = simple_generator_with_asyncio_coroutine_dec()
    print(sg_aio_dec)
    print("simple generator instance of collections.abc.Iterable : " + str(isinstance(sg_aio_dec, Iterable)))
    print("simple generator instance of collections.abc.Awaitable : " + str(isinstance(sg_aio_dec, Awaitable)))
    print("simple generator instance of types.Generator : " + str(isinstance(sg_aio_dec, types.GeneratorType)))
    print("simple generator instance of types.CoroutineType : " + str(isinstance(sg_aio_dec, types.CoroutineType)))
    print("simple generator instance of asyncio.iscoroutine : " + str(asyncio.iscoroutine(sg_aio_dec)))
    print("simple generator instance of asyncio.iscoroutinefunction : " + str(
        asyncio.iscoroutinefunction(simple_generator_with_asyncio_coroutine_dec)))
    print("simple generator instance of inspect.iscoroutine : " + str(inspect.iscoroutine(sg_aio_dec)))
    print("generator instance of inspect.iscoroutinefunction : " + str(
        inspect.iscoroutinefunction(simple_generator_with_asyncio_coroutine_dec)))
    print("simple generator instance of inspect.isawaitable : " + str(inspect.isawaitable(sg_aio_dec)))
    print("\n\n")

    sg_types_dec = simple_generator_with_types_coroutine_dec()
    print(sg_types_dec)
    print("simple generator instance of collections.abc.Iterable : " + str(isinstance(sg_types_dec, Iterable)))
    print("simple generator instance of collections.abc.Awaitable : " + str(isinstance(sg_types_dec, Awaitable)))
    print("simple generator instance of types.Generator : " + str(isinstance(sg_types_dec, types.GeneratorType)))
    print("simple generator instance of types.CoroutineType : " + str(isinstance(sg_types_dec, types.CoroutineType)))
    print("simple generator instance of asyncio.iscoroutine : " + str(asyncio.iscoroutine(sg_types_dec)))
    print("simple generator instance of asyncio.iscoroutinefunction : " + str(
        asyncio.iscoroutinefunction(simple_generator_with_types_coroutine_dec)))
    print("simple generator instance of inspect.iscoroutine : " + str(inspect.iscoroutine(sg_types_dec)))
    print("generator instance of inspect.iscoroutinefunction : " + str(
        inspect.iscoroutinefunction(simple_generator_with_types_coroutine_dec)))
    print("simple generator instance of inspect.isawaitable : " + str(inspect.isawaitable(sg_types_dec)))
    print("\n\n")

    gbc = generator_based_coroutine()
    print(gbc)
    print("generator instance of collections.abc.Iterable : " + str(isinstance(gbc, Iterable)))
    print("generator instance of collections.abc.Awaitable : " + str(isinstance(gbc, Awaitable)))
    print("generator instance of types.Generator : " + str(isinstance(gbc, types.GeneratorType)))
    print("generator instance of types.CoroutineType : " + str(isinstance(gbc, types.CoroutineType)))
    print("generator instance of asyncio.iscoroutine : " + str(asyncio.iscoroutine(gbc)))
    print("generator instance of asyncio.iscoroutinefunction : " + str(
        asyncio.iscoroutinefunction(generator_based_coroutine)))
    print("generator instance of inspect.iscoroutine : " + str(inspect.iscoroutine(gbc)))
    print("generator instance of inspect.iscoroutinefunction : " + str(
        inspect.iscoroutinefunction(generator_based_coroutine)))
    print("generator instance of inspect.isawaitable : " + str(inspect.isawaitable(gbc)))
    print("\n\n")

    gbc_aio_dec = generator_based_coroutine_with_asyncio_coroutine_dec()
    print(gbc_aio_dec)
    print("generator instance of collections.abc.Iterable : " + str(isinstance(gbc_aio_dec, Iterable)))
    print("generator instance of collections.abc.Awaitable : " + str(isinstance(gbc_aio_dec, Awaitable)))
    print("generator instance of types.Generator : " + str(isinstance(gbc_aio_dec, types.GeneratorType)))
    print("generator instance of types.CoroutineType : " + str(isinstance(gbc_aio_dec, types.CoroutineType)))
    print("generator instance of asyncio.iscoroutine : " + str(asyncio.iscoroutine(gbc_aio_dec)))
    print("generator instance of asyncio.iscoroutinefunction : " + str(
        asyncio.iscoroutinefunction(generator_based_coroutine_with_asyncio_coroutine_dec)))
    print("generator instance of inspect.iscoroutine : " + str(inspect.iscoroutine(gbc_aio_dec)))
    print("generator instance of inspect.iscoroutinefunction : " + str(
        inspect.iscoroutinefunction(generator_based_coroutine_with_asyncio_coroutine_dec)))
    print("generator instance of inspect.isawaitable : " + str(inspect.isawaitable(gbc_aio_dec)))
    print("\n\n")

    gbc_types_dec = generator_based_coroutine_with_types_coroutine_dec()
    print(gbc_types_dec)
    print("generator instance of collections.abc.Iterable : " + str(isinstance(gbc_types_dec, Iterable)))
    print("generator instance of collections.abc.Awaitable : " + str(isinstance(gbc_types_dec, Awaitable)))
    print("generator instance of types.Generator : " + str(isinstance(gbc_types_dec, types.GeneratorType)))
    print("generator instance of types.CoroutineType : " + str(isinstance(gbc_types_dec, types.CoroutineType)))
    print("generator instance of asyncio.iscoroutine : " + str(asyncio.iscoroutine(gbc_types_dec)))
    print("generator instance of asyncio.iscoroutinefunction : " + str(
        asyncio.iscoroutinefunction(generator_based_coroutine_with_types_coroutine_dec)))
    print("generator instance of inspect.iscoroutine : " + str(inspect.iscoroutine(gbc_types_dec)))
    print("generator instance of inspect.iscoroutinefunction : " + str(
        inspect.iscoroutinefunction(generator_based_coroutine_with_types_coroutine_dec)))
    print("generator instance of inspect.isawaitable : " + str(inspect.isawaitable(gbc_types_dec)))
    print("\n\n")

    nc = native_coroutine()
    print("native coro instance of collections.abc.Iterable : " + str(isinstance(nc, Iterable)))
    print("native coro instance of collections.abc.Awaitable : " + str(isinstance(nc, Awaitable)))
    print("native coro instance of types.Generator : " + str(isinstance(nc, types.GeneratorType)))
    print("native coro instance of types.CoroutineType : " + str(isinstance(nc, types.CoroutineType)))
    print("native coro instance of asyncio.iscoroutine : " + str(asyncio.iscoroutine(nc)))
    print("native coro instance of asyncio.iscoroutinefunction : " + str(asyncio.iscoroutinefunction(native_coroutine)))
    print("native coro instance of inspect.iscoroutine : " + str(inspect.iscoroutine(nc)))
    print("generator instance of inspect.iscoroutinefunction : " + str(
        inspect.iscoroutinefunction(native_coroutine)))
    print("native coro instance of inspect.isawaitable : " + str(inspect.isawaitable(nc)))
    print(nc)
    print("\n\n")
