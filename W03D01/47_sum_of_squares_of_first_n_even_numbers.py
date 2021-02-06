"""Program to print Sum of Squares of first n even numbers"""

def print_sum_of_squares(n):
    """Print sum of squares of first n natural even numbers"""
    print(f"The sum of squares of first n natural even numbers")
    sum=0
    s=""
    for i in range(1,n+1):
        if i%2 ==0:
            sum = sum + i*i
            s = s + str(i*i) 
            if i!= n:
                s = s + " + "
    #print(f"Sum of squares of {n} even numbers is: {sum}")
    print(f"Sum of squares of 1 to {n} --> ({s}) is {sum}")

def main():
    print_sum_of_squares(5)
    print_sum_of_squares(10)

main()

"""
Output
c:/akademize/W01D01/srm-pylearn/W03D01/47_sum_of_squares_of_first_n_even_numbers.py
The sum of squares of first n natural even numbers
Sum of squares of 1 to 5 --> (4 + 16 + ) is 20
The sum of squares of first n natural even numbers
Sum of squares of 1 to 10 --> (4 + 16 + 36 + 64 + 100) is 220
"""