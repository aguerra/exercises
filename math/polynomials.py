"""Choose a representation and write a function to add polynomials."""

from itertools import starmap, zip_longest


def add(*args):
    """Return a list.

    Each element is the coefficient of x^index.

    >>> add([1, 1, 2], [0, 2, -1, 3])
    [1, 3, 1, 3]

    >>> add([1, 5, -1, 2], [0, -2, 1, 3], [1, 2, 3, 4, 5])
    [2, 5, 3, 9, 5]
    """
    it = zip_longest(*args, fillvalue=0)
    def _sum(*args): return sum(args)
    return list(starmap(_sum, it))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
