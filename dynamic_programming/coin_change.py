"""
Determine the fewest number of coins you can use to make a certain
amount if you have coins of a certain set of denominations. You can
use any quantity of each denomination and assume the denominations are
given in increasing order of value. Alternatives:

* Use one coin of the highest denomination, the number of coins used
  goes up by one.
* Don’t use any coin of the highest denomination, move to next one
  and the number of coins used stays the same.

Recurrence relation: f(i, a) = min(f(i, a-d[i]) + 1, f(i-1, a)).
"""

import math


def naive(amount, coins):
    """Return the number of coins.

    >>> naive(9, [1, 2])
    5

    >>> naive(10, [1, 3, 4])
    3

    >>> naive(5, [1, 5])
    1

    >>> naive(16, [1, 5, 12, 19])
    4

    >>> naive(42, [1, 21, 25])
    2
    """
    if amount == 0:
        return 0
    if amount < 0 or len(coins) == 0:
        return math.inf
    use_it = 1 + naive(amount - coins[-1], coins)
    skip_it = naive(amount, coins[:-1])
    return min(use_it, skip_it)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
