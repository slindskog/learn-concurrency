def is_prime(i):
    if i == 1 or i == 2 or i == 3:
        return True
    k = 2
    while k <= i / 2:
        if i % k == 0:
            return False
        k += 1

    return True


def get_primes():
    i = 1
    while True:
        if is_prime(i):
            yield i
        i += 1


if __name__ == '__main__':
    gen = get_primes()

    # A generator function returns a generator object which is an iterator
    print(iter(gen) is gen)

    print(next(gen))
    print(gen.__next__())
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
