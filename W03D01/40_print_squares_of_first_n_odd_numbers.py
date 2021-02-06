"""Program to print squares of first n odd numbers"""

def print_squares(n):
    """Function to print squares of n odd numbers"""
    print(f"This function prints squares of odd numbers under {n}")
    for i in range(1,n):
        if (i%2 != 0):
            print(f"Square of {i} is {i*i}")

def main():
    """Main function calling the print function"""
    print_squares(15)
    print_squares(25)

main()

"""Output
1D01/srm-pylearn/W03D01/40_print_squares_of_first_n_odd_numbers.py
This function prints squares of odd numbers under 15
Square of 1 is 1
Square of 3 is 9
Square of 5 is 25
Square of 7 is 49
Square of 9 is 81
Square of 11 is 121
Square of 13 is 169
This function prints squares of odd numbers under 25
Square of 1 is 1
Square of 3 is 9
Square of 5 is 25
Square of 7 is 49
Square of 9 is 81
Square of 11 is 121
Square of 13 is 169
Square of 15 is 225
Square of 17 is 289
Square of 19 is 361
Square of 21 is 441
Square of 23 is 529
"""