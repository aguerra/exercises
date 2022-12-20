"""
Write a function to find the maximum number of distinct elements
(non-repeating) after removing n elements from collection.
"""


def max_after_removing(iterable, n):
    """
    >>> max_after_removing([], 1)
    0

    >>> max_after_removing([1, 2, 3, 4], 2)
    2

    >>> max_after_removing([1, 1, 1, 4], 3)
    1

    >>> max_after_removing([1, 1, 1, 4], 2)
    2

    >>> max_after_removing([5, 7, 5, 5, 1, 2, 2], 4)
    3

    >>> max_after_removing([5, 7, 5, 5, 1, 2, 2], 1)
    4
    """
    if not iterable:
        return 0

    total = len(iterable)
    unique = len(set(iterable))
    return total - max(total-unique, n)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
