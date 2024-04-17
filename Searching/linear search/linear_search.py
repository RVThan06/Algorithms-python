"""Program to perform linear search. This algorithm has a o(n)
    complexity during worst case since it has to iterate through
    every other element. Suitable for small datasets.
"""


def linear_search(my_array: list, key: int) -> int:
    """To search and return item from list O(n)."""

    for index,_ in enumerate(my_array):
        if my_array[index] == key:
            return index

    return -1


def print_index(position: int, key: int) -> None:
    """To print index of searhced element."""

    if position != -1:
        print(f"Key: {key} found at index: {position}")
        return

    print(f"Key: {key} not found")


# main code
array = [87, 13, 24, 12, 89, 21, 12, 40]

key_array = [13, 40, 87, -2, -67]

for value in key_array:
    print_index(linear_search(array, value), value)
