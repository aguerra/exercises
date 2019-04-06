from collections import Counter
from heapq import heapify, heappop, heappush


def max_distinct_elements(iterable, n):
    """
    Find the maximum number of distinct elements (non-repeating)
    after removing n elements from the iterable.

    >>> max_distinct_elements([3, 4, 7, 7, 7, 6], 3)
    3

    >>> max_distinct_elements([80, 80, 100000, 80, 80, 80, 80, 12345678], 4)
    3

    >>> max_distinct_elements('123456789', 5)
    4
    """
    counter = Counter(iterable)
    heap = [-v for v in counter.values()]
    heapify(heap)
    while n > 0:
        item = heappop(heap)
        item += 1
        if item:
            heappush(heap, item)
        n -= 1
    return len(heap)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
