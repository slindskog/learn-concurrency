import multiprocessing


class Test:
    value = 777


def process_task():
    print(Test.value)


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')

    # Change the value of Test.value before creating a new process
    Test.value = 999
    process = multiprocessing.Process(target=process_task, name='process-1')
    process.start()
    process.join()
