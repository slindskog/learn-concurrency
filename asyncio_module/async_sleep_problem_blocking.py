import time
from threading import Thread, current_thread


def sync_sleep(sleep_for):
    time.sleep(sleep_for)
    print(f"Sleeping completed in {current_thread().getName()}")


if __name__ == '__main__':
    start = time.time()
    threads = []
    for _ in range(5):
        threads.append(Thread(target=sync_sleep, args=(5,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f"Main program exiting after running for {time.time() - start}")
