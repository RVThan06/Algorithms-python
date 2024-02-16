"""Quicksort algorithm implmentation in python."""

# standard library import



def partition(my_array: list, start: int, end: int) -> int:
    """Fucntion to sort using pivot and return index of pivot."""

    # last elemeent in list in pivot, p_index is the start before iteration
    p_index = start

    # iterate to compare all element from start till element before pivot
    # iteration does not include pivot which is the last element
    for i in range(start, end):

        # if item less than pivot swap it with item at p_index
        if my_array[i] < my_array[end]:
            temp = my_array[i]
            my_array[i] = my_array[p_index]
            my_array[p_index] = temp
            p_index = p_index + 1

    # upon completing sorting based on pivot, insert pivot in middle
    # swap pivot with p_index element
    temp = my_array[p_index]
    my_array[p_index] = my_array[end]
    my_array[end] = temp

    return p_index


def quicksort(my_array: list, start: int, end: list) -> None:
    """To divide the arary and recursively call partition to sort."""

    # if only there are at least 2 elements in subaray
    if start<end:
        # partition and sort to the left and right and get pivot index
        pivot = partition(my_array, start, end)
        # call partition recursively to sort left subarray of pivot
        quicksort(my_array, start, pivot-1)
        # call partition recursively to sort right subarray of pivot
        quicksort(my_array, pivot+1, end)

    # remainder: we pass the same array so, rearrangement happens without
    # splicing the arrays into subarrays in memory, instead we provide
    # a range for the indices


# main function calls

# 1. create an unsorted list
my_list = [85, 28, 34, 64, 22, 31, 59, 38, 72, 94, 27, 16, 13, 11, 39, 11]
print("Before sorting: ", my_list)

# 2. Call the sorting function on the list
# pass the first(0) and last index(len-1) of the list
quicksort(my_list, 0, len(my_list)-1)\

# 3. print the sorted list
print("After sorting: ", my_list)
