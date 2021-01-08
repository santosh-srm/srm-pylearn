"""28_max_of_three_numbers.py"""

print("----Finding max of 3 numbers----")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if (num1 > num2):
    if (num1 > num3):
        print(f'The max number is {num1}')
    else:
        print(f'The max number is {num3}')
else:
    if (num2 > num3):
        print(f'The max number is {num2}')
    else:
        print(f'The max number is {num3}')


"""
Output
----Finding max of 3 numbers----
Enter the first number: 2
Enter the second number: 3
Enter the third number: 4
The max number is 4
PS C:\akademize\W01D01> & C:/Users/santosh/AppData/Local/Programs/Python/Python39/python.exe c:/akademize/W01D01/srm-pylearn/28_max_of_three_numbers.py
----Finding max of 3 numbers----
Enter the first number: 4
Enter the second number: 3
Enter the third number: 5
The max number is 5
"""        