"""15_simple_interest.py"""

print("-- This is a Simple Interest Program --")
p = int(input("Enter the Principle Amount Value: "))
n = int(input("Enter the number of months: "))
r = int(input("Provide the rate of interest: "))
si = (p*n*r)//100

print (f'The Simple Interest for the provided values is: {si}')

"""
Output
Enter the Principle Amount Value: 200000
Enter the number of months: 24
Provide the rate of interest: 2
The Simple Interest for the provided values is: 96000
"""