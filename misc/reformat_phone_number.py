"""
You are given a string representing a phone number.

It has at least two digits, spaces and/or dashes. Write a function to reformat
the phone number in such a way that the digits are grouped in blocks of length
n separated by single dashes.
"""

from itertools import islice


def reformat_phone_number(phone_number, n):
    """Return the reformatted phone number.

    >>> reformat_phone_number('00-44  48 5555 8361', 3)
    '004-448-555-583-61'

    >>> reformat_phone_number('0  -  22 1985--324', 3)
    '022-198-532-4'

    >>> reformat_phone_number('123456789', 2)
    '12-34-56-78-9'

    >>> reformat_phone_number('42', 3)
    '42'
    """
    digits = (x for x in phone_number if x.isdigit())
    it = iter(lambda: ''.join(islice(digits, n)), '')
    return '-'.join(it)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
