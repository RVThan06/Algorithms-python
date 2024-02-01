"""Bubble sort algorithm."""


# standard library imports
import time


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


# basic sorting
list_a = [23,12,10,1,24,56,91,13,-5,-12]
print(f"List before sorting: {list_a}")
bubble_sort(list_a)
print(f"List after sorting: {list_a}")

# worst case scenario sorting
list_b = [x for x in range(10000,0,-1)]
print("Before sorting")
print(list_b[9990:])
start = time.time()
bubble_sort(list_b)
end = time.time()
print(f"After sorting Time elapsed: {end - start}s")
print(list_b[9990:])