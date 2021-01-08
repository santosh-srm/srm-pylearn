"""21_even_or_odd.py"""

n = int(input("Enter a number: "))
rem = n % 2
print('Even: ', rem == 0)
print('Odd : ', rem != 0)

if (rem == 0):
    print(f"The number {n} is an even number")
else:
    print(f"The number {n} is an odd number")

"""
Output
21_even_or_odd.py
Enter a number: 10
Even:  True
Odd :  False
The number 10 is an even number

21_even_or_odd.py
Enter a number: 9
Even:  False
Odd :  True
The number 9 is an odd number
"""