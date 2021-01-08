"""17_powers.py"""

a = int(input("Enter first number: "))
b = int(input("Enter the exponent: "))

print(f'Method 1: using ** {a}^{b} = {a**b}')
print(f'Method 2: using power func {a}^{b} = {pow(a,b)}') 
#print(f'Method 3: {a}^{b} = {math.pow(a,b)}')


"""
Output
Enter first number: 3
Enter the exponent: 5
Method 1: using ** 3^5 = 243
Method 2: using power func 3^5 = 243

"""

