"""Program to print squares of first n even numbers"""

def print_squares(n):
    """Function to print squares of n even numbers"""
    print(f"This function prints squares of even numbers under {n}")
    for i in range(1,n):
        if (i%2 == 0):
            print(f"Square of {i} is {i*i}")

def main():
    """Main function calling the print function"""
    print_squares(10)
    print_squares(20)

main()

"""
output
This function prints squares of even numbers under 10
Square of 2 is 4
Square of 4 is 16
Square of 6 is 36
Square of 8 is 64
This function prints squares of even numbers under 20
Square of 2 is 4
Square of 4 is 16
Square of 6 is 36
Square of 8 is 64
Square of 10 is 100
Square of 12 is 144
Square of 14 is 196
Square of 16 is 256
Square of 18 is 324
"""