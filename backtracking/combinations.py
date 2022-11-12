"""
You are given two integers, n and k.

Return all possible combinations of k numbers out of the range [1, n].
"""


def recursive(n, k):
    """Return combinations as a list.

    >>> recursive(3, 4)
    []

    >>> recursive(3, 1)
    [[1], [2], [3]]

    >>> recursive(3, 2)
    [[1, 2], [1, 3], [2, 3]]

    >>> recursive(3, 3)
    [[1, 2, 3]]

    >>> recursive(4, 3)
    [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
    """
    result = []

    def _recursive(start, path):
        if len(path) == k:
            result.append(list(path))
            return

        for i in range(start, n+1):
            path.append(i)
            _recursive(i+1, path)
            path.pop()

    _recursive(1, [])
    return result


def iterative(n, k):
    """Return combinations as a generator.

    >>> list(iterative(3, 4))
    []

    >>> list(iterative(3, 1))
    [[1], [2], [3]]

    >>> list(iterative(3, 2))
    [[1, 2], [1, 3], [2, 3]]

    >>> list(iterative(3, 3))
    [[1, 2, 3]]

    >>> list(iterative(4, 3))
    [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
    """
    path = [1]
    while path:
        if path[-1] > n:
            path.pop()
            if path:
                path[-1] += 1
        elif len(path) == k:
            yield list(path)
            path[-1] += 1
        else:
            path.append(path[-1]+1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
