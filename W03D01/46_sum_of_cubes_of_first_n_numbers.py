"""Program to print Sum of cubes of first n numbers"""

def print_sum_of_cubes(n):
    """Print sum of cubes of first n natural numbers"""
    print(f"The sum of cube of first n natural numbers")
    sum=0
    s=""
    for i in range(1,n+1):
        sum = sum + i*i*i
        s = s + str(i*i*i) 
        if i!= n:
            s = s + " + "
    #print(f"Sum of cubes of {n} numbers is: {sum}")
    print(f"Sum of cubes of 1 to {n} --> ({s}) is {sum}")

def main():
    print_sum_of_cubes(5)
    print_sum_of_cubes(10)

main()

"""
Output
c:/akademize/W01D01/srm-pylearn/W03D01/46_sum_of_cubes_of_first_n_numbers.py
The sum of cube of first n natural numbers
Sum of cubes of 1 to 5 --> (1 + 8 + 27 + 64 + 125) is 225
The sum of cube of first n natural numbers
Sum of cubes of 1 to 10 --> (1 + 8 + 27 + 64 + 125 + 216 + 343 + 512 + 729 + 1000) is 3025
"""