"""Program to Print all Evens below n."""

def print_even(n):
    """Print Even Numbers within n"""
    print(f'Print Even Numbers less than {n}')
    print("**********************************")
    for i in range(1, n):
        if (i % 2 == 0):
            print(i)
    print("End of Program")

def main():
        """Print Even Numbers by calling function"""
        print_even(10)
        print_even(25)

main()

"""Output
Print Even Numbers less than 10
**********************************
2
4
6
8
End of Program
Print Even Numbers less than 25
**********************************
2
4
6
8
10
12
14
16
18
20
22
24
End of Program
"""