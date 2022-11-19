"""Linked list implementation."""

missing = object()


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return repr(self.value)


class LinkedList:
    def __init__(self, iterable=[]):
        it = iter(iterable)
        first = next(it, missing)
        node = None if first is missing else Node(first)
        self.head = node
        for item in it:
            node.next = Node(item)
            node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        """Return the length of the linked list.

        >>> len(LinkedList())
        0

        >>> len(LinkedList(range(5)))
        5
        """
        return sum(1 for node in self)

    def __repr__(self):
        """Return the representation of the linked list.

        >>> repr(LinkedList())
        ''

        >>> repr(LinkedList(range(5)))
        '0->1->2->3->4'

        >>> repr(LinkedList([1, None, 2]))
        '1->None->2'
        """
        return "->".join(repr(node) for node in self)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
