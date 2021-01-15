from threading import Thread, current_thread


class MyTask(Thread):
    def __init__(self):
        Thread.__init__(self, name="subclassThread", args=(2, 3))

    def run(self):
        print(f"{current_thread().getName()} is executing.")


if __name__ == '__main__':
    my_task = MyTask()
    my_task.start()  # Start the thread
    my_task.join()  # Wait for the thread to complete
    print(f"{current_thread().getName()} exiting")
