"""Python implementation of exponential search."""


# standard library
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


def binary_search(my_array: list, key: int) -> int:
    """To search for a given key"""

    low = 0
    high = len(my_array) - 1
    present = False

    while low <= high:
        mid = (low + high)//2

        if my_array[mid] == key:
            present = True
            return mid

        if key < my_array[mid]:
            high = mid - 1
        else:
            low = mid + 1

    if not present:
        return -1


def exponential_search(my_array: list, key: int) -> int:
    """Algorithm implementing exponential search."""

    # check if key at first index
    if my_array[0] == key:
        return 0

    index = 1
    prev_index = 1
    power = 1

    while index < len(my_array):

        if key <= my_array[index]:

            # if match key at index then return the fucntion
            if my_array[index] == key:
                return index

            # else binary search within current block
            found_index = binary_search(my_array[prev_index:index+1], key=key)

            # key not found in current block
            if found_index == -1:
                return found_index

            # this is index in original array not subarray, return when key is found in block
            return found_index+prev_index

        # update the index exponentially
        prev_index = index
        index = int(math.pow(2, power))
        if index > len(my_array):
            index = len(my_array) - 1
        power = power + 1


def print_index(position: int, key: int) -> None:
    """To print index of searhced element."""

    if position != -1:
        print(f"Key: {key} found at index: {position}")
        return

    print(f"Key: {key} not found")


# code implementation

list_a = [1,2,3,4,5,6,7,8,9,10]
print(list_a)
key_a = [3, 7, -26]
for i in key_a:
    print_index(exponential_search(list_a, i), i)
print()


# list with negative numbers
list_b = [23,12,10,1,24,56,91,13,-5,-12,1000,33,43]
bubble_sort(list_b)
print(list_b)
key_b = [43, 1, -12, 1000, 21, 13, 59]
for i in key_b:
    print_index(exponential_search(list_b, i), i)
