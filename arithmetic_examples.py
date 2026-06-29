"""Simple examples of Python arithmetic operators.

Run this file with: `python arithmetic_examples.py`
"""

def demonstrate_arithmetic():
    a = 12
    b = 5

    print('a =', a, 'b =', b)

    # Addition
    print('Addition: a + b =', a + b)

    # Subtraction
    print('Subtraction: a - b =', a - b)

    # Multiplication
    print('Multiplication: a * b =', a * b)

    # Division (float)
    print('Division: a / b =', a / b)

    # Floor division
    print('Floor division: a // b =', a // b)

    # Modulus (remainder)
    print('Modulus: a % b =', a % b)

    # Exponentiation
    print('Exponentiation: a ** b =', a ** b)

    # Unary plus/minus
    print('Unary plus: +a =', +a)
    print('Unary minus: -a =', -a)

    # Combined operators (in-place)
    c = 3
    print('\nStart c =', c)
    c += 4
    print('After c += 4 ->', c)
    c *= 2
    print('After c *= 2 ->', c)


if __name__ == '__main__':
    demonstrate_arithmetic()
