"""Program to print Sum of Squares of first n odd numbers"""

def print_sum_of_squares(n):
    """Print sum of squares of first n natural odd numbers"""
    print(f"The sum of squares of first n natural odd numbers")
    sum=0
    s=""
    for i in range(1,n+1):
        if i%2 != 0:
            sum = sum + i*i
            s = s + str(i*i) 
            if i!= n:
                s = s + " + "
    #print(f"Sum of squares of {n} odd numbers is: {sum}")
    print(f"Sum of squares of 1 to {n} --> ({s}) is {sum}")

def main():
    print_sum_of_squares(5)
    print_sum_of_squares(10)

main()

"""
output
c:/akademize/W01D01/srm-pylearn/W03D01/48_sum_of_squares_of_first_n_odd_numbers.py
The sum of squares of first n natural odd numbers
Sum of squares of 1 to 5 --> (1 + 9 + 25) is 35
The sum of squares of first n natural odd numbers
Sum of squares of 1 to 10 --> (1 + 9 + 25 + 49 + 81 + ) is 165
"""