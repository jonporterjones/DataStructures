import linked_list
import pytest


def test_linked_list():

    test_list = [1, 3, 5, 7, 9, 11, 13, 17]

    first_item = linked_list.Item.construct_from_list(test_list)
    
    assert isinstance(first_item, linked_list.Item)

    result_list = first_item.traverse_items()

    assert test_list == result_list
