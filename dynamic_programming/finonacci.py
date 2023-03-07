"""
f(0) = 0, f(1) = 1
f(n) = f(n-1) + f(n-2)
"""

from functools import cache


@cache
def memoized(n):
    """Return the nth Fibonacci number.

    >>> memoized(0)
    0

    >>> memoized(1)
    1

    >>> memoized(2)
    1

    >>> memoized(5)
    5

    >>> memoized(9)
    34

    >>> memoized(17)
    1597
    """
    if n < 2:
        return n
    return memoized(n-1) + memoized(n-2)


def bottom_up(n):
    """Return the nth Fibonacci number.

    >>> bottom_up(0)
    0

    >>> bottom_up(1)
    1

    >>> bottom_up(2)
    1

    >>> bottom_up(5)
    5

    >>> bottom_up(9)
    34

    >>> bottom_up(17)
    1597
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


if __name__ == '__main__':
    import doctest
    doctest.testmod()
