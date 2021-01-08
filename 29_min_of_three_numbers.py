"""29_min_of_three_numbers.py"""

print ("****Finding Minimum of 3 Numbers****")

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number:"))

if (num1 < num2):
    if(num2 < num3):
        print("The minimum of entered 3 numbers is: ", num1)
    else:
        print("The minumum of entered 3 numbers is: ", num3)
else:
    if(num3 < num2):
        print(f'The minimum of entered 3 numbers is: {num3}')
    else:
        print(f'The minimum of entered 3 numbers is: {num2}')

"""
****Finding Minimum of 3 Numbers****
Enter the first number: 4
Enter the second number: 3
Enter the third number:5
The minimum of entered 3 numbers is: 3
c:/akademize/W01D01/srm-pylearn/29_min_of_three_numbers.py
****Finding Minimum of 3 Numbers****
Enter the first number: 34
Enter the second number: 56
Enter the third number:23
The minumum of entered 3 numbers is:  23

"""