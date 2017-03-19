"""Validate that a given square is valid.

Checks that this is either a simple square (``0`` or ``1``), or
a split square (a list of 4 items, each being a simple square or
a split square).

A simple square is valid::

    >>> validate(0)
    True

A split square of four simple filled squares is valid::

    >>> validate([1, 1, 1, 1])
    True

We can nest split and simple squares::

    >>> validate([1, 0, [1, [0, 0, 0, 0], 1, [1, 1, 1, 1]], 1])
    True

    >>> validate([1, [1, 0, 1, [0, [0, 0, 0, 0], 1, 1]], [1, 0, 1, 0], 1])
    True

Simple squares must be either 0 (empty) or 1 (filled)::

    >>> validate(2)
    False

Split squares must contain exactly four parts::

    >>> validate([1, 1, 1, 1, 1])
    False

    >>> validate([1, 0, [1, [0, 0, 0, 0, 1], 1, [1, 1, 1, 1]], 1])
    False

    >>> validate([1, [1, 0, 1, [0, [0, 0, 0], 1, 1]], [1, 0, 1, 0], 1])
    False

"""


def validate(s):
    """Validate that a given square is valid.."""

    # base case: square is 1 or 0
    if s == 1 or s == 0:
        return True

    # list of length 4
    if isinstance(s, list) and len(s) == 4:

        # idea one: fail fast
        for i in s:
            if not validate(i):
                return False
        return True

        # idea 2: "and" the results ALSO fail fast
        # return (validate(s[0]) and 
        #         validate(s[1]) and 
        #         validate(s[2]) and 
        #         validate(s[3]))
        # OR
        # return all([validate(i) for i in s])

        # idea 3: multiply the results: will not return boolean
        # return (validate(s[0]) * 
        #         validate(s[1]) * 
        #         validate(s[2]) * 
        #         validate(s[3]))

    # not one of our numbers or list of length 4
    # another base case
    return False


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS; THAT'S SUPER-VALID WORK!\n"