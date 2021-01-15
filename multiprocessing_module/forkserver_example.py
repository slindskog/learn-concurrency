import time
import multiprocessing


def process_task():
    # block the new process
    time.sleep(1000 * 1000)


# Windows only supports spawn
if __name__ == '__main__':
    multiprocessing.set_start_method('forkserver')

    process = multiprocessing.Process(target=process_task, name='process-1')
    process.start()
    print("New process created")
    process.join()

    # ps -aef | grep python
    # four python processes:
    # parent, child, forkserver, semaphore tracker
