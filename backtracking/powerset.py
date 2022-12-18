"""Given a set, generates its power set."""


def recursive(s):
    """Return a list with all subsets.

    >>> recursive(set())
    [set()]

    >>> recursive({1})
    [set(), {1}]

    >>> recursive({1, 2})
    [set(), {1}, {1, 2}, {2}]

    >>> recursive({1, 2, 3})
    [set(), {1}, {1, 2}, {1, 2, 3}, {1, 3}, {2}, {2, 3}, {3}]
    """
    result = []
    tmp = list(s)

    def _recursive(start, path):
        result.append(set(path))

        for i in range(start, len(tmp)):
            path.append(tmp[i])
            _recursive(i+1, path)
            path.pop()

    _recursive(0, [])
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
