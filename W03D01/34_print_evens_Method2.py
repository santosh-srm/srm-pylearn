"""Print Evens Below the given number"""

def print_even(n):
    """Print even numbers below the given number"""
    print(f'Print Even Numbers below {n}')
    print("*****-----*****-----*****-----")
    for i in range(0,n,2):
        print(i)
    print("\n")    

def main():
    print_even(10)
    print_even(15)
    print("End of Program")
main()

"""Output
Print Even Numbers below 10
*****-----*****-----*****-----
0
2
4
6
8


Print Even Numbers below 15
*****-----*****-----*****-----
0
2
4
6
8
10
12
14


End of Program
"""