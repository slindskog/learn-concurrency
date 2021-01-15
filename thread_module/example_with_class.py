class ExampleClass:
    def __init__(self, val):
        print("Initialization")
        self.val = val

    def display(self):
        print(self.val)

    def __enter__(self):
        print("Enter invoked")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit invoked")


if __name__ == '__main__':
    with ExampleClass("Hello World!") as example:
        example.display()
