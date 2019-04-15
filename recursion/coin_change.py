import math


def coin_change(n, denom):
    """
    You have an infinite amount of k different denominations of coins.
    You need to find the minimum number of coins to possess a value of n
    dollars.

    >>> coin_change(9, [1, 2])
    5

    >>> coin_change(10, [1, 3, 4])
    3

    >>> coin_change(5, [1, 5])
    1
    """
    result = math.inf
    if n <= 0:
        return 0
    for d in denom:
        if n >= d:
            result = min(result, 1 + coin_change(n-d, denom))
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
