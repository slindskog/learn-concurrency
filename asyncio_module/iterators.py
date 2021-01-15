if __name__ == '__main__':
    items = [1, 2, 3]

    # Get iterator of items using __iter__()
    it = items.__iter__()
    print(f"Iterator of items: {it}")

    # Get member elements of items using __getitem__()
    print(f"Iterator of items: {items.__getitem__(2)}")

    # Iterator returns itself when passed to the iter function
    print(f"it is iter(it) = {it is iter(it)}")

    # Get another iterator for items using the build in iter() method
    it_another = iter(items)
    print(f"it_another: {it_another}")

    print("iteration using iterator in a for loop")
    # Iterate using the iterator
    for element in it_another:
        print(element)

    print("iteration using iterable in a for loop")
    # Iterate using the iterable
    for element in items:
        print(element)
