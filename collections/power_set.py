from functools import reduce


def powerset(iterable):
    """
    Write a function that generates the power set of an iterable.

    >>> sorted(powerset('ab'))
    [[], ['a'], ['a', 'b'], ['b']]

    >>> sorted(powerset([]))
    [[]]
    """
    return reduce(lambda r, x: r + [item + [x] for item in r], iterable, [[]])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
