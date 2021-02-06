"""Factorial Program -- Different logic"""

def print_factorial(n):
    """Print factorial."""
    fact = 1
    """
        Iterating backwards
        start at n
        stop  at 1
        Decrement i by 1
    """

    for i in range(n, 0, -1):
        fact = fact * i

    print(f"{n}! = {fact}")


def main():
    
    print_factorial(5)
    print_factorial(8)
    print_factorial(10)


main()

"""
Output
c:/akademize/W01D01/srm-pylearn/W03D01/50_factorialprogram.py
5! = 120
8! = 40320
10! = 3628800
"""