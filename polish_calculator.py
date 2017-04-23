"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num21

def calc(s):
    """Evaluate expression."""

    stack = s.split()
    
    num2 = int(stack.pop())

    while stack:
        
        num1 = int(stack.pop())

        operator = stack.pop()

        if operator == '+':
            num2 = num1 + num2 
        elif operator == '-':
            num2 = num1 - num2
        elif operator == '*':
            num2 = num1 * num2
        elif operator == '/':
            num2 = num1 / num2

    return num2
                

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. ***\n"
