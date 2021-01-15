def generate_numbers():
    i = 0
    while True:
        i += 1
        yield i
        k = yield
        print(f"Received in generator function: {k}")


if __name__ == "__main__":
    generator = generate_numbers()

    # The first iteration happens outside the loop
    k = next(generator)
    print(f"Received in main function: {k}")

    for i in range(0, 11):
        # The noop operation required to move the generator
        # from the first yield to the second yield statement
        next(generator)

        # send will both pass in the value to the generator
        # function and also yield the next value from the generator
        k = generator.send(i + 50)
        print(f"Received in main function: {k}")
