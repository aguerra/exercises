"""
Write a function to return the unique elements of a list
preserving order.
"""


def unique(iterable):
    """Return a generator.

    >>> list(unique([1, 1, 2, 3, 4, 5, 4, 6]))
    [1, 2, 3, 4, 5, 6]

    >>> list(unique([]))
    []
    """
    seen = set()
    seen_add = seen.add
    for item in iterable:
        if item not in seen:
            seen_add(item)
            yield item


if __name__ == '__main__':
    import doctest
    doctest.testmod()
