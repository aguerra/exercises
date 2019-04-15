def knapsack01(weight_left, items, index=0):
    """
    Return the maximum value that can be put in a knapsack.
    Items are represented by tuples (value, weight).

    >>> knapsack01(50, [(60, 10), (100, 20), (120, 30)])
    220

    >>> knapsack01(3, [(10, 1), (20, 1), (30, 1)])
    60

    >>> knapsack01(0, [(10, 1), (20, 1), (30, 1)])
    0
    """
    if index == len(items):
        return 0
    result = knapsack01(weight_left, items, index+1)
    current = items[index]
    if current[1] <= weight_left:
        result = max(
            result,
            current[0] + knapsack01(weight_left - current[1], items, index+1),
        )
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
