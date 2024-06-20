import random

import binary_tree


def test_binary_tree():
    """Test the binary tree."""

    # seed a list of 50 random ints between 1 and 100, do not allow duplicates.
    test_list = []
    while len(test_list) < 50:
        num = random.randint(1, 100)
        if num not in test_list:
            test_list.append(num)

    # create the binary tree
    binary_tree_test = binary_tree.BinaryTree(test_list)

    # search for a value I know is bad
    binary_search_result = binary_tree_test.binary_search(765)
    assert not binary_search_result[0] 

    # search for a value I know is good
    test_value = random.choice(test_list)
    binary_search_result = binary_tree_test.binary_search(test_value)
    assert binary_search_result[0]

    # search for a value that may or may not be in the test_list
    test_value = random.randint(1, 100)
    assert len(binary_search_result[1]) > 0
