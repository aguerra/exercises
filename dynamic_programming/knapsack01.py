"""
Given a set of items, each with a weight and a value, determine which items to
include in the collection so that the total weight is less than or equal to a
given limit and the total value is as large as possible. We can either put an
item completely into the collection or cannot put it at all (01).

Recurrence relation: f(i, l) = max(f(i+1, l-w[i]) + v[i], f(i+1, l))
"""

from functools import cache


@cache
def memoized(limit, items, index=0):
    """Return the total value.

    Items are represented by tuples (value, weight).

    >>> memoized(50, ((60, 10), (100, 20), (120, 30)))
    220

    >>> memoized(3, ((10, 1), (30, 1), (20, 1)))
    60

    >>> memoized(0, ((10, 1), (20, 1), (30, 1)))
    0
    """
    if index == len(items):
        return 0
    value, weight = items[index]
    index += 1
    result = memoized(limit, items, index)
    if weight <= limit:
        result = max(
            result,
            value + memoized(limit-weight, items, index)
        )
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
