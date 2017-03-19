"""Produce new square adding two inputs squares.

Two simple squares can be added::

    >>> s1 = 0
    >>> s2 = 1

    >>> add(s1, s2)
    1

A simple square and a split square can be added::

    >>> s1 = 0
    >>> s2 = [1, 0, 1, 0]

    >>> add(s1, s2)
    [1, 0, 1, 0]

Two split squares can be added::

    >>> s1 = [0, 0, 0, 1]
    >>> s2 = [0, 1, 0, 1]

    >>> add(s1, s2)
    [0, 1, 0, 1]

Nested squares can be added::

    >>> s1 = [0, [1, 1, 1, [0, 0, 0, 0]], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

Unevenly-nested squares can be added::

    >>> s1 = [0, [1, 1, 1, 0           ], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> s1 = [0, [1, 1, 1, 1                      ], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, [0, 0, 0, 0], 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [1, [1, 1, 1, 1], 1, 1]], [1, 0, 1, 0], 1]
"""


def add(s1, s2):
    """Produce new split square adding two input squares."""

    # base case: comparing two numbers
    if isinstance(s1, int) and isinstance(s2, int):
        return s1 | s2

    # if they're not both lists: 
    if isinstance(s1, int):
        s1 = [s1, s1, s1, s1]

    elif isinstance(s2, int):
        s2 = [s2, s2, s2, s2]

    # now they are both lists
    return [add(i1, i2) for i1, i2 in zip(s1, s2)]



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS; YOU'RE A RECURSION WIZARD!\n"
