def generate_numbers():
    i = 0
    while True:
        i += 1
        yield i
        k = yield
        print(k)


if __name__ == '__main__':
    gen = generate_numbers()

    item = next(gen)
    print(f"Received in main script: {item}")

    # Nothing is received by the generator function
    item = gen.send(5)
    print(f"Received in main script: {item}")

    # The second send is succesful
    item = gen.send(5)
    print(f"Received in main script: {item}")
