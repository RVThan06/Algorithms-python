"""Interpolation search in python."""


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


def inrterpolation_search(my_array: list, key: int) -> tuple:
    """To perform interpolation search and return index. O(log(logn))"""

    # proceed with searching algorithm
    high = len(my_array) - 1
    low = 0
    probe = 1

    # check if only one item left and also if the target is within the range of high and lows
    while low <= high and my_array[low]<=key<=my_array[high]:

        # probe equation
        mid = low + ((high - low) * (key - my_array[low])) // (my_array[high] - my_array[low])

        # condition to check for the key based on probe
        if my_array[mid] == key:
            return mid,probe
        elif key < my_array[mid]:
            high = mid - 1
        elif key > my_array[mid]:
            low = mid + 1

        probe = probe + 1

    return -1,probe


def print_index(probing: tuple, key: int) -> None:
    """To print index of searhced element."""

    if probing[0] != -1:
        print(f"Key: {key} found at index: {probing[0]} after {probing[1]} probes.")
        return

    print(f"Key: {key} not found after {probing[1]} probes.")


# code implementation

# more uniformyl distributed data less probing
list_a = [1,2,3,4,5,6,7,9,10]
for i in list_a:
    probe = inrterpolation_search(list_a, i)
    print_index(probe, i)
print()

# less uniformly distributed data, so more probing
list_b = [23,12,10,1,24,56,91,13,-5,-12]
bubble_sort(list_b)

list_c = list_b + [-2, -45, 29]

for i in list_c:
    probe = inrterpolation_search(list_b, i)
    print_index(probe, i)
