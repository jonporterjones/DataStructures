"""Unit tests for all the sorting algorithms in the sorting package."""
import pytest

from sorting.src import sorts


@pytest.fixture(scope="module")
def create_list():
    """create a list to be sorted, fixture allows for re-use in any sorting algorithm."""
    list_to_sort = [87, 66, 71, 77, 7, 33, 56, 99, 11, 44]
    sorted_list_answer = [7, 11, 33, 44, 56, 66, 71, 77, 87, 99]

    return (list_to_sort, sorted_list_answer)

@pytest.fixture(scope="module")
def create_simple_list():
    """create a list to be sorted, fixture allows for re-use in any sorting algorithm."""
    list_to_sort = [87]
    sorted_list_answer = [87]

    return (list_to_sort, sorted_list_answer)

def test_bubble_sort(create_list):
    """Test the bubble sort algorithm."""
    list_to_sort, sorted_list_answer = create_list

    sorted_list = sorts.bubble_sort(list_to_sort)

    assert (sorted_list == sorted_list_answer)

def test_bubble_sort_simple(create_simple_list):
    """Test the bubble sort algorithm."""
    list_to_sort, sorted_list_answer = create_simple_list

    sorted_list = sorts.bubble_sort(list_to_sort)

    assert (sorted_list == sorted_list_answer)