  
"""Factorial."""

def print_factorial(n):
    """Program to print Factorial"""
    fact=1
    for i in range(2, n+1):
        fact=fact*i
    print(f"{n}! = {fact}")

def main():
    """ Calling Print Factorial Function """
    print_factorial(5)
    print_factorial(8)
    print_factorial(10)

main()

"""
Output
c:/akademize/W01D01/srm-pylearn/W03D01/49_factorialprogram.py
5! = 120
8! = 40320
10! = 3628800
"""

