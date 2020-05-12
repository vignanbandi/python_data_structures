"""
GCD -- Finds the greatest common denominator by using Euclid's algorithm.
"""


def gcd(a, b):
    if b > a:
        a, b = b, a
    reminder = a % b
    if reminder != 0:
        a, b = b, reminder
        return gcd(a, b)
    else:
        return b


print(gcd(20, 8))
print(gcd(60, 96))
