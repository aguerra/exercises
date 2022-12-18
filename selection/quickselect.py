"""Quickselect implementations."""


def recursive(iterable, k):
    """Return the kth smallest element.

    >>> recursive([], 1) is None
    True

    >>> recursive([1, 2, 3, 4], 2)
    2

    >>> recursive([4, 3, 2, 1], 3)
    3

    >>> recursive([7, 8, 1, 10, 2], 4)
    8

    >>> recursive([1, 1, 1, 1, 2], 2)
    2

    >>> recursive([1, 1, 1, 1, 2], 3) is None
    True
    """
    if not iterable:
        return None
    pivot = next(iter(iterable))
    less, greater = [], []

    for item in iterable:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            greater.append(item)

    tmp = len(less) + 1
    if tmp == k:
        return pivot
    elif tmp < k:
        return recursive(greater, k - tmp)
    else:
        return recursive(less, k)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
