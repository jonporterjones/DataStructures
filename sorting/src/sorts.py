"""Functions to demonstrate various sorting algorithms."""

from typing import List


def bubble_sort(list_to_sort: List[int]) -> List[int]:
    """Perform  a bubble sort."""

    # Each time through outer loop the smallest value will bubble to the top of the list (via the inner loop).
    # Each subsequent pass through the outer loop requires one list comparison.
    # is_sorted will act to short circuit comparisons
    #  If no swaps are made in a pass through the outer loop then it is sorted and we can break out.
    is_sorted = False
    for i in range(0, len(list_to_sort) - 1):
        if is_sorted:
            break
        is_sorted = True
        for j in range(len(list_to_sort) - 1, i, -1):
            if list_to_sort[j] < list_to_sort[j - 1]:
                list_to_sort[j], list_to_sort[j-1] = list_to_sort[j-1], list_to_sort[j] # swap
                is_sorted = False

    return list_to_sort
