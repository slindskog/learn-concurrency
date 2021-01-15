import sys

if __name__ == '__main__':
    # Declare a variable
    some_var = "Educative"

    # Check reference count
    print(sys.getrefcount(some_var))

    # Create another reference to some_var
    another_var = some_var

    # Verify the incremented reference count
    print(sys.getrefcount(some_var))
