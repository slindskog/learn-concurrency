from threading import Thread, current_thread


def thread_task(a, b, c, key1, key2):
    print(f"{current_thread().getName()} received the arguments: {a} {b} {c} {key1} {key2}")


if __name__ == '__main__':
    my_thread = Thread(
        group=None,  # reserved
        target=thread_task,  # callable object
        name="demoThread",  # name of the thread
        args=(1, 2, 3),  # arguments passed to the target
        kwargs={  # dictionary of keyword arguments
            'key1': 777,
            'key2': 111
        },
        daemon=None  # Set to True to make the thread a daemon
    )
    my_thread.start()  # Start the thread
    my_thread.join()  # Wait for the thread to complete
