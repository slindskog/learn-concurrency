def get_item():
    try:
        yield 5
    except GeneratorExit:
        print("GeneratorExit exception raised")


if __name__ == "__main__":
    gen = get_item()

    print(next(gen))

    # Uncomment to close generator before Main exits
    # gen.close()

    print("Main exiting")
