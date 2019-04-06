from itertools import islice


def reformat_phone_number(phone_number, n):
    """
    You are given a string representing a phone number: at least two
    digits, spaces and/or dashes. Write a function to reformat the
    phone number in such a way that the digits are grouped in blocks
    of length three separated by single dashes.

    >>> reformat_phone_number('00-44  48 5555 8361', 3)
    '004-448-555-583-61'

    >>> reformat_phone_number('0  -  22 1985--324', 3)
    '022-198-532-4'

    >>> reformat_phone_number('123456789', 3)
    '123-456-789'

    >>> reformat_phone_number('42', 3)
    '42'
    """
    numbers = (n for n in phone_number if n.isdigit())
    func = lambda: ''.join(islice(numbers, n))
    grouper = iter(func, '')
    return '-'.join(g for g in grouper)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
