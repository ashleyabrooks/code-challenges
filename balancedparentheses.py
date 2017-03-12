"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""

    total_parens = 0

    for char in phrase:
        if char == '(':
            total_parens += 1
        elif char == ')':
            total_parens -= 1

    if total_parens == 0:
        return True

    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. ***\n"
