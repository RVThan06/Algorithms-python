"""Program to merge sort an array in python.

    The array is diveded into 2 till 2 single item
    array is obtained, the value is compared between
    both single array to sort it.

    There is no return statement in functions because
    the list object in memeory is directly modified without needing
    to be copied and returned
"""


# standard library imports
import time


def merge_sort(lst: list) -> None:
    """To divide the array and sort using merge()."""

    if len(lst) > 1:

        mid = len(lst)//2
        # divide the array into right and left sub-array
        right = lst[:mid]
        left = lst[mid:len(lst)]

        # sort the list object directly so no need to return a list
        merge_sort(left)
        merge_sort(right)
        # upon dividing merge the sorted list
        merge(lst, left, right)


def merge(nums: list, left: list, right: list) -> None:
    """To sort and merge the sorted list."""

    i = 0
    j = 0
    length = len(nums)

    for k in range(length):

        # left and right are not empty so compare and merge value
        if i<len(left) and j<len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i = i + 1
            else:
                nums[k] = right[j]
                j = j + 1

        # if left is empty, then merge everything in right
        elif i == len(left):
            nums[k] = right[j]
            j = j + 1

        # if right list is empty, then merge everything in left
        elif j == len(right):
            nums[k] = left[i]
            i = i + 1


# sorting a simple list
my_list = [34,23,56,23,67,23,11,36,55]
print("Before sorting")
print(my_list)
start = time.time()
merge_sort(my_list)
end = time.time()
print(f"After sorting Time elapsed: {end - start}")
print(my_list)

# sorting a list of 1 million to check runtime (worst case)
new_list = [x for x in range(1000000,0,-1)]
print("Before sorting")
print(new_list[999990:])
start = time.time()
merge_sort(new_list)
end = time.time()
print(f"After sorting Time elapsed: {end - start}s")
print(new_list[999990:])
