"""Python implementation of jump search."""

# standard library import
import math


def bubble_sort(lst: list) -> None:
    """To bubble sort in ascending order."""

    list_len = len(lst)

    # from 0 to n-1 element iteration only
    for k in range(list_len-1):
        swapped = False

        # check swappinnfrom 0 to n-1-k
        for i in range(list_len-1-k):

            key = lst[i]
            if lst[i+1] < key:
                # swap the element
                lst[i] = lst[i+1]
                lst[i+1] = key
                swapped = True

        # break if loop is fully sorted
        if swapped is False:
            break


def jump_search(my_array: list, key: int) -> None:
    """Jump search algorithm."""

    index = 0
    block_size = int(math.sqrt(len(my_array)))

    # checks from 0 t0 len - 1
    while index <= len(my_array)-1:

        j = index+block_size-1

        # adjust the maximum index to prevent indexing out of range
        if j >= len(my_array):
            j = len(my_array) - 1

        # find the block where key could be located within
        if key <= my_array[j]:

            # if key is at the jump index itself then end the function
            if my_array[j] == key:
                return index

            # linear search within block less than the current jump index index+block_size
            for i in range(index, j):
                if my_array[i] == key:
                    return i

            # not in the lower block so element not found
            return -1

        # if key larger than value at jump index, we jump to next by a block size
        index = index + block_size

    # if key is larger than all items in the array
    return -1



def print_index(position: int, key: int) -> None:
    """To print index of searhced element."""

    if position != -1:
        print(f"Key: {key} found at index: {position}")
        return

    print(f"Key: {key} not found")


# code implementation

list_a = [1,2,3,4,5,6,7,8,9,10]
print(list_a)
key_a = [4, 10, -26]
for key in key_a:
    print_index(jump_search(list_a, key), key)
print()

# list with negative numbers
list_b = [23,12,10,1,24,56,91,13,-5,-12,1000,33,43]
bubble_sort(list_b)
print(list_b)
key_b = [10, 1000, 43, -7, -2, -12]
for key in key_b:
    print_index(jump_search(list_b, key), key)
