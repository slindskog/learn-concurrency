def generator_function():
    while True:
        item = yield
        print(f"Received {item}")


if __name__ == '__main__':
    gen = generator_function()

    # next(gen)
    # Start a generator by sending None, which is not received but advances the generator function to the first
    # yield statement
    gen.send(None)

    gen.send(37)
