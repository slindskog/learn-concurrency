import multiprocessing

from multiprocessing_module import spawn_example2


def process_task():
    print("I am a child process")


if __name__ == '__main__':
    # Change the method to 'spawn' and verify that modules
    # are reimported in the child process
    multiprocessing.set_start_method("spawn")
    process = multiprocessing.Process(target=process_task)
    process.start()
    process.join()
    print("I am a parent process")
