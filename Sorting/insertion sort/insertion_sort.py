"""This program demonstrates insertion sort algorithm.

    Insertion sort has a runtime of c1n^2
    thus the speed of sorting is propotional to
    n^2 which is the number of items squared
"""


# standard library import



def sort_ascending(my_list: list) -> None:
    """sorts the list in ascending order."""

    for j in range(1, len(my_list)):
        key = my_list[j]
        i = j - 1

        # the original list object is modified
        while i >= 0 and key < my_list[i]:
            my_list[i+1] = my_list[i] # swap
            my_list[i] = key
            i = i-1


def sort_descending(my_list: list) -> None:
    """sorts the list in descending order."""

    for j in range(1, len(my_list)):
        key = my_list[j]
        i = j - 1

        # the original list object is modified
        while i >= 0 and key > my_list[i]:
            my_list[i+1] = my_list[i] # swap
            my_list[i] = key
            i = i-1


def ascending_recursive(my_list: list) -> None:
    """To sort recursively in ascending order."""

    length = len(my_list)

    if length > 1:

        # last element
        key = my_list[length-1]
        # recursion list now has less 1 item
        sorted_list = ascending_recursive(my_list[0:length-1])
        # append the sorted list to the original list
        my_list[0:length-1] = sorted_list
        i = length-2

        while i >= 0 and key < my_list[i]:
            my_list[i+1] = my_list[i]
            my_list[i] = key
            i = i-1
        # print sorted sub-list
        print(my_list)

    return my_list


# sorting list in ascending order
nums = [31,41,59,26,41,58]
sort_ascending(nums)
print(nums)

# sorting list in descending order
sort_descending(nums)
print(nums)

# sorting list in ascending order recursively
nums = [9,8,7,6,5,4,3]
ascending_recursive(nums)
print(nums)

# # sorting at 100000 to test runtime
# new_list = [x for x in range(100000,0,-1)]
# sort_ascending(new_list)
# print(new_list[99990:])
