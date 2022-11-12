"""
Write a function to randomly choose n items from a stream.

Each element must have an equal probability of being chosen.
"""

import random


def simple(iterable, n):
    """Return the sample as a list. This is called Algorithm R.

    The idea is to pick the first n items and after that choose the next ones
    based on a probability p of replacing the first ones. We can calculate p
    for the first item after n:

    (1 - p/n) = p -> p = n/(n+1)

    Using induction you can prove that p = n/(n+i), which is the
    probability of a random number on [0, n+i) to be < n.

    >>> simple([], 1)
    []

    >>> simple([1, 2], 3)
    [1, 2]

    >>> simple("a", 1)
    ['a']

    >>> len(simple(range(100), 5))
    5
    """
    reservoir = []
    for i, item in enumerate(iterable):
        if i < n:
            reservoir.append(item)
        else:
            r = random.randrange(0, i)
            if r < n:
                reservoir[r] = item
    return reservoir


if __name__ == '__main__':
    import doctest
    doctest.testmod()
