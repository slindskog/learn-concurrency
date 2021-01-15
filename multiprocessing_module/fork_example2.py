import os
import multiprocessing

file_desc = None


def process_task():
    # Write to the file in a child process
    file_desc.write(f"\nline written by child process with pid: {os.getpid()}")
    file_desc.flush()


# Windows only supports spawn
if __name__ == '__main__':
    # Create a file descriptor in the parent process
    file_desc = open("sample.txt", 'w')
    file_desc.write(f"\nline written by parent process iwth pid: {os.getpid()}")
    file_desc.flush()

    multiprocessing.set_start_method("fork")

    process = multiprocessing.Process(target=process_task)
    process.start()
    process.join()
    file_desc.close()

    # Read and print the contents of the file
    with open("sample.txt", "r") as file_desc:
        print(file_desc.read())

    os.remove("sample.txt")
