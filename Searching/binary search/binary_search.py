"""Python implementation of binary search. This algorithm requires
    the array to be sorted. The time complexity is O(logn) as the akgorithm
    uses divide and conquer approch and it halfs the array size in every iteration.

"""

# standard library imports


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
    """To search for a given key and return its index. O(logn)"""

    low = 0
    high = len(my_array) - 1

    while low <= high:
        mid = (low + high)//2

        if my_array[mid] == key:
            return mid

        if key < my_array[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def print_index(position: int, key: int) -> None:
    """To print index of searhced element."""

    if position != -1:
        print(f"Key: {key} found at index: {position}")
        return

    print(f"Key: {key} not found")



# code implementation

list_a = [23, 12, 10, 1, 24, 56, 91, 13, -5, -12]
bubble_sort(list_a)
print(list_a)

key_array = [23, 24, 56, 91, -5, -12, -1, 4]

for key in key_array:
    print_index(binary_search(list_a, key), key)
