"""Program to print squares of first n numbers"""

def print_squares(n):
    """Function to print squares of n numbers"""
    print(f"This function prints squares of {n} numbers")
    for i in range(1,n):
        print(i*i)

def main():
    """Main function calling the print function"""
    print_squares(5)
    print_squares(8)

main()

"""
output
This function prints squares of 5 numbers
1
4
9
16
This function prints squares of 8 numbers
1
4
9
16
25
36
49
"""