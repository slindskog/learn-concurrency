import random
import asyncio
from threading import Thread, current_thread


async def do_something_important(sleep_for):
    print(f"Is event loop running in thread {current_thread().getName()} = {asyncio.get_event_loop().is_running()}")
    await asyncio.sleep(sleep_for)


def launch_event_loops():
    # Get a new event loop
    loop = asyncio.new_event_loop()

    # Set the event loop for the current thread
    asyncio.set_event_loop(loop)

    # Run a coroutine on the event loop
    loop.run_until_complete(do_something_important(random.randint(1, 5)))

    # Remember to close the loop
    loop.close()


if __name__ == '__main__':
    t1 = Thread(target=launch_event_loops)
    t2 = Thread(target=launch_event_loops)

    t1.start()
    t2.start()

    print(f"Is event loop running in thread {current_thread().getName()} = {asyncio.get_event_loop().is_running()}")

    t1.join()
    t2.join()
