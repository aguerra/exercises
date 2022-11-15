"""Quicksort implementations."""


def recursive(iterable):
    """Return a sorted list.

    >>> recursive([])
    []

    >>> recursive([1, 2, 3, 4])
    [1, 2, 3, 4]

    >>> recursive([4, 3, 2, 1])
    [1, 2, 3, 4]

    >>> recursive([7, 8, 1, 10, 2])
    [1, 2, 7, 8, 10]

    >>> recursive({9, 10, 0, 46, 20})
    [0, 9, 10, 20, 46]

    >>> recursive({3: 1, 2: 2})
    [2, 3]
    """
    if not iterable:
        return []
    it = iter(iterable)
    pivot = next(it)
    less, greater = [], []

    for item in it:
        if item <= pivot:
            less.append(item)
        else:
            greater.append(item)

    return recursive(less) + [pivot] + recursive(greater)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
