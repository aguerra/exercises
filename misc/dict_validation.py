"""
Write a function to validate a dict with a set of rules:
- the value for key a should be a sorted list of integers.
- the value for key b should be an integer greater than 0.
Assume that values have the right schema: list of integers and integer.
It should return all the reasons the dict is invalid.
Adding new validations should be easy.
"""

from functools import partial
from itertools import pairwise
from operator import le


def _is_gt_zero(d, key):
    value = d[key]
    is_valid = value > 0
    error = '' if is_valid else f'Value for {key} is <= 0'
    return is_valid, error


def _is_sorted(d, key):
    value = d[key]
    it = pairwise(value)
    is_valid = all(le(a, b) for a, b in it)
    error = '' if is_valid else f'Value for {key} is not sorted'
    return is_valid, error


validations = [
    partial(_is_sorted, key='a'),
    partial(_is_gt_zero, key='b')
]


def is_valid_dict(d, validations=validations):
    """Return a tuple (boolean, errors).

    >>> is_valid_dict({'a': [1, 2], 'b': 1})
    (True, [])

    >>> is_valid_dict({'a': [1, 2, 42, 3], 'b': 1})
    (False, ['Value for a is not sorted'])

    >>> is_valid_dict({'a': [1, 2, 42, 3], 'b': -1})
    (False, ['Value for a is not sorted', 'Value for b is <= 0'])
    """
    results = [f(d) for f in validations]
    is_valid = all(result[0] for result in results)
    errors = [result[1] for result in results if not result[0]]
    return is_valid, errors


if __name__ == '__main__':
    import doctest
    doctest.testmod()
