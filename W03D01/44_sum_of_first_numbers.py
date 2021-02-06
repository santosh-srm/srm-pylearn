"""Program to print sum of first n natural numbers"""

def print_sum(n):
    """Function to print sum of n natural numbers"""
    print(f"This program prints sum of {n} natural numbers")
    sum=0
    s=""
    for i in range(1,n+1):
        sum = sum + i
        s = s + str(i)
        if i!=n:
            s = s + " + "
    print(f"{s} is {sum}")

def main():
    print_sum(10)
    print_sum(15)

main()

"""
Output
c:/akademize/W01D01/srm-pylearn/W03D01/44_sum_of_first_numbers.py
This program prints sum of 10 natural numbers
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 is 55
This program prints sum of 15 natural numbers
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 is 120
"""