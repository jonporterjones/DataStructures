"""Create a binary tree.

Internal nodes will have values that may be valid traversal results.
Leaf nodes will simply have no left/right edges.
"""
import statistics
from typing import List, Tuple


class BinaryTree():
    """Store a binary tree which is a collection of nodes."""

    def __init__(self, ints: List[int]):
        """Initialize."""
        self.ints = ints
        self.root_node = Node()
        self._seed_tree(ints, self.root_node)

    def _seed_tree(self, ints: List[int], node: "Node"):
        """Private method to seed a binary tree from a list of ints."""
        midpoint = statistics.mode(ints)
        node.set_value(midpoint)

        left_values = [value for value in ints if value < midpoint]
        right_values = [value for value in ints if value > midpoint]

        if left_values:
            left_node = Node()
            node.set_left_edge(left_node)
            self._seed_tree(left_values, left_node)

        if right_values:
            right_node = Node()
            node.set_right_edge(right_node)
            self._seed_tree(right_values, right_node)

    def binary_search(self, value: int) -> Tuple[bool, List[int]]:
        """Search for a value in the tree.

        Args:
            value (int): The value to search for.

        Returns:
            Tuple[bool, List[int]]: boolean if found, and a list of nodes traversed.
        """

        found_value, nodes = self.root_node._search_node(value)

        return found_value, nodes
    
class Node():
    """A node in a binary tree."""

    def __init__(self):
        """Initialize a node."""
        self.value = None
        self.left_edge = None
        self.right_edge = None

    def set_value(self, value: int):
        """Set the value"""
        self.value = value

    def set_left_edge(self, node: "Node"):
        """Set the next item."""
        self.left_edge = node

    def set_right_edge(self, node: "Node"):
        """Set the next item."""
        self.right_edge = node

    def _search_node(self, value: int, nodes: List[int] = []) -> bool:
        """Private method to recursively search through nodes."""
        is_found = False

        if self.value == value:
            is_found = True

        nodes.append(self.value)
        if value < self.value:
            if self.left_edge:
                is_found, nodes = self.left_edge._search_node(value, nodes)
            
        if value > self.value:
            if self.right_edge:
                is_found, nodes = self.right_edge._search_node(value, nodes)

        return is_found, nodes
