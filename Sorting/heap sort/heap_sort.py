"""Implemnetatio of heap sort algorithm in python."""


# standard library imports
import math as mt


def heapify_list(my_heap: list) -> None:
    """Heapify the entire heap."""

    # find the internal nodes(non-leaf nodes)
    nodes = mt.floor(len(my_heap)/2) - 1

    # heapify each internal node from deepest internal node to root node
    # this ensures as we reach higher internal nodes the left and right subtree is a heap
    for index in range(nodes, -1, -1):
        heapify(index, my_heap)


def heapify(index:int, my_heap: list) -> None:
    """Heapify from parent(deleted node) to child."""

    # compare parent node with the child nodes till leaf
    length = len(my_heap)
    largest = index
    left_child = 2*index + 1
    right_child = 2*index + 2

    # run algo as long as child nodes exist, find the largest child
    if right_child < length and my_heap[right_child] > my_heap[index]:
        largest = right_child

    if left_child < length and my_heap[left_child] > my_heap[largest]:
        largest = left_child

    # swap parent with child if child is larger
    if largest != index:
        temp = my_heap[index]
        my_heap[index] = my_heap[largest]
        my_heap[largest] = temp
        # next recursion move to child node just swaped, so we go to lower nodes to heapify
        heapify(largest, my_heap)


def heap_sort(my_heap: list) -> list:
    """To heap sort the list."""

    index = 0
    sorted_list = []

    while len(my_heap) > 0:

        # first item in heap is largest so extract it
        sorted_list.insert(0, my_heap[0])
        # swap root node/first item (deleted) with last node
        my_heap[0] = my_heap[-1]
        # remove last node, so value deleted
        my_heap.pop()
        # heapify from the root since the root node value was deleted
        heapify(index, my_heap)

    return sorted_list



# main code

# . create an unsorted list
unsorted_list = [35, 33, 42, 10, 14, 11, 19, 27, 44, 26, 31, 99, 27]

# 2. heapify the list to create max heap
heapify_list(unsorted_list)

# 3. heap sort the max heap to get a sorted list in return
sorted_list  = heap_sort(unsorted_list)
print(sorted_list)
