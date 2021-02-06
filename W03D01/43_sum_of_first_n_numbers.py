"""Program to find sum of first n natural numbers.py"""

def print_sum(n):
    """Print sum of Natural Numbers below given number"""
    print(f" THis program prints sum of {n} natural numbers")
    sum=0
    for i in range(1, n):
        sum=sum+i
    print(f"The sum of {n} natural numbers is: {sum}")

def main():
    print_sum(15)
    print_sum(20)

main()

"""
Output

c:/akademize/W01D01/srm-pylearn/W03D01/43_sum_of_first_n_numbers.py
 THis program prints sum of 15 natural numbers
The sum of 15 natural numbers is: 105
 THis program prints sum of 20 natural numbers
The sum of 20 natural numbers is: 190

"""