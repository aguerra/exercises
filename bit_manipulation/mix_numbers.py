def mix_numbers(n, m, i, j):
    """
    You are given two numbers, n and m, and two bit positions, i and j.  Write
    a method to insert m into n such that m starts at bit j and ends at bit i.
    You can assume that the bits j through i have enough space to fit all of m.

    >>> mix_numbers(1024, 19, 2, 6) # 10000000000 10011 -> 10001001100
    1100

    >>> mix_numbers(500, 33, 3, 8) # 111110100 100001 -> 100001100
    268
    """
    ones = ~0
    left_mask = ones << (j + 1)
    right_mask = (1 << i) - 1
    mask = left_mask | right_mask
    cleared = n & mask
    shifted = m << i
    return cleared | shifted


if __name__ == '__main__':
    import doctest
    doctest.testmod()
