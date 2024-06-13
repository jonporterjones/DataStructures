"""Create and traverse a linked list."""

from typing import List


class Item():
    """A linked list item."""

    def __init__(self, value: int):
        """Initialize an item."""
        self.value = value
        self.next = None

    def set_next(self, item: "Item"):
        """Set the next item."""
        self.next = item

    def traverse_items(self):
        """Traverse linked list items and return resulting list."""

        # deconstruct the linked list back into a list.
        list = []
        list.append(self.value)

        linked_item = self
        while linked_item.next:
            linked_item = linked_item.next
            list.append(linked_item.value)

        return list

    @staticmethod
    def construct_from_list(list: List):
        """Generate a linked list from a list of items.

        Returns:
            Item: The first item in the list, used to traverse linked list.
        """
        first_item = Item(value=list[0])
        previous_item = first_item
        for list_item in list[1:]:
            item = Item(value=list_item)
            previous_item.set_next(item)
            previous_item = item

        return first_item
