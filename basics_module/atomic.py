import dis

count = 0


def increment():
    global count
    count += 1


if __name__ == '__main__':
    dis.dis(increment)
