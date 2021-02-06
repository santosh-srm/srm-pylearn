"""Program to print Sum of Squares of first n numbers"""

def print_sum_of_squares(n):
    """Print sum of squares of first n natural numbers"""
    print(f"The sum of squares of first n natural numbers")
    sum=0
    s=""
    for i in range(1,n+1):
        sum = sum + i*i
        s = s + str(i*i) 
        if i!= n:
            s = s + " + "
    #print(f"Sum of squares of {n} numbers is: {sum}")
    print(f"Sum of squares of 1 to {n} --> ({s}) is {sum}")

def main():
    print_sum_of_squares(5)
    print_sum_of_squares(10)

main()

"""
Output

c:/akademize/W01D01/srm-pylearn/W03D01/45_sum_of_squares_of_first_n_numbers.py
The sum of squares of first n natural numbers
Sum of squares of 1 to 5 --> (1 + 4 + 9 + 16 + 25) is 55
The sum of squares of first n natural numbers
Sum of squares of 1 to 10 --> (1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100) is 385
"""