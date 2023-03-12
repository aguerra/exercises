"""
There's an array of 10,000 16-bit values, how do you count the bits most
efficiently.
"""

lookup_table = [bin(n).count("1") for n in range(256)]


def bit_count(array):
    """Return the bit count.

    >>> bit_count([])
    0

    >>> bit_count([0, 1])
    1

    >>> bit_count([2, 65535])
    17
    """
    s = 0
    for item in array:
        s += lookup_table[item >> 8] + lookup_table[item & 0xff]
    return s


if __name__ == '__main__':
    import doctest
    doctest.testmod()
