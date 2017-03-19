"""Print each square on a new line.

A simple square will only be one line::

    >>> printout(0)
    0

    >>> printout(1)
    1

A split square will use four lines::

    >>> printout([0, 1, 0, 1])
    0
    1
    0
    1

A nested split square will use one line per square::

    >>> printout([0, 0, 0, [1, 1, 1, 1]])
    0
    0
    0
    1
    1
    1
    1

Of course, these can nested deeply and still work::

    >>> printout([0, 0, 0, [1, 1, 1, [0, 0, 0, [1, 1, 1, 1]]]])
    0
    0
    0
    1
    1
    1
    0
    0
    0
    1
    1
    1
    1
"""


def printout(s):
    """Print each square on a new line."""

    # base case
    if not isinstance(s, list):
        print s

    # recursive case
    else:
        for i in s:
            printout(i)

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS; NICE JOB!\n"
