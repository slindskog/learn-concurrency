import time
import math
import random

random.seed(42)
scratch = None


def merge_sort(start, end, items):
    global scratch

    if start == end:
        return
    mid = start + math.floor((end - start) / 2)

    # Sort the first half
    merge_sort(start, mid, items)

    # Sort the second half
    merge_sort(mid + 1, end, items)

    # Merge the two sorted arrays
    i = start
    j = mid + 1

    for k in range(start, end + 1):
        scratch[k] = items[k]

    k = start
    while k <= end:
        if i <= mid and j <= end:
            items[k] = min(scratch[i], scratch[j])

            if items[k] == scratch[i]:
                i += 1
            else:
                j += 1
        elif i <= mid and j > end:
            items[k] = scratch[i]
        else:
            items[k] = scratch[j]
            j += 1
        k += 1


def create_data(size):
    unsorted_list = [random.randint(0, 1000) for _ in range(size)]
    return unsorted_list


if __name__ == '__main__':
    then = time.time()
    my_list = create_data(10_000)
    scratch = [None] * 10_000
    merge_sort(0, len(my_list) - 1, my_list)
    print(my_list)
    print(f"Total time: {time.time() - then}")
