"""Python program to implement selection."""



def selection_sort(my_array: list) -> None:
    """To sort an array in ascending order."""

    length = len(my_array)

    for i in range(length):

        minimum = i
        for j in range (i+1, length):
            if my_array[minimum] > my_array[j]:
                minimum = j

        temp = my_array[i]
        my_array[i] = my_array[minimum]
        my_array[minimum] = temp


# main codes

# before sorting
my_array = [87, 45, 34, 88, 11, 24, 69, 62, 19, 10, 72]
print(my_array)

# after sorting
selection_sort(my_array)
print(my_array)
