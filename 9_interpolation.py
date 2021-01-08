"""09_string_interpolation.py"""

a = 20
b = 30

sum = a+b

print (f'Method 1: {a} + {b} = {sum}')
print ("Method 2:",a, "+",b,  "=", sum)
print ("Method 3: " +str(a)+ " + " +str(b) + " = " +str(sum))


"""
Output
Method 1: 20 + 30 = 50
Method 2: 20 + 30 = 50
Method 3: 20 + 30 = 50
"""