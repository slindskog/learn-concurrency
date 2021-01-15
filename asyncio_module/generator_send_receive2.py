def generate_numbers():
    i = 0
    while True:
        i += 1
        k = (yield i)  # Can do this but not good
        print(k)
        # Instead: Use generators to generate values and coroutines to consume values
        # Generators that receive values are called coroutines


if __name__ == '__main__':
    gen = generate_numbers()

    item = gen.send(None)
    print(f"Received in main script: {item}")

    for i in range(5):
        item = gen.send(55 + i)
        print(f"Received in main script: {item}")
