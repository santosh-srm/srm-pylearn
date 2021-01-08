"""30_elif.py -- ElIf conditions """

age = int(input("Enter age: "))

if(age <= 2):
    print("It is an infant")
elif (age <= 12):
    print("It is a child")
elif (age <= 19):
    print("It is a Teen")
elif (age <= 60):
    print("It is an adult")
else:
    print("Sr. Citizen Category")

"""
Output
Enter age: 55
It is an adult
PS C:\akademize\W01D01> & C:/Users/santosh/AppData/Local/Programs/Python/Python39/python.exe c:/akademize/W01D01/srm-pylearn/30_elif.py
Enter age: 1
It is an infant
PS C:\akademize\W01D01> & C:/Users/santosh/AppData/Local/Programs/Python/Python39/python.exe c:/akademize/W01D01/srm-pylearn/30_elif.py
Enter age: 15
It is a Teen
PS C:\akademize\W01D01> & C:/Users/santosh/AppData/Local/Programs/Python/Python39/python.exe c:/akademize/W01D01/srm-pylearn/30_elif.py
Enter age: 4
It is a child
PS C:\akademize\W01D01> & C:/Users/santosh/AppData/Local/Programs/Python/Python39/python.exe c:/akademize/W01D01/srm-pylearn/30_elif.py
Enter age: 75
Sr. Citizen Category
"""