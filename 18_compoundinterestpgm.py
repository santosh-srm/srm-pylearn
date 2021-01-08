"""18_compound_interest.py."""

p=int(input("Enter the principal amount: "))
r=float(input("Enter the rate of interst: "))
n=int(input("Enter the duration for which interest is applied per time period: "))
#t=int(input("Enter the number of time period elapsed: "))
rate=(1+r)**n
fv=p * rate


print(f"the compound interest for the details provided is: {fv}")

"""
Output

Enter the principal amount: 1000
Enter the rate of interst: .005
Enter the duration for which interest is applied per time period: 12
the compound interest for the details provided is: 1061.6778118644984
"""