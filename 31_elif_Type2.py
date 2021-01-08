"""30_elif.py -- Nested conditional statements """

age = int(input("Enter age: "))

if(age <= 2):
    print("It is an infant")
else:
    if (age <= 12):
        print("It is a child")
    else:
        if (age <= 19):
            print("It is a Teen")
        else:
            if (age <= 60):
                print("It is an adult")
            else:
                print("Sr. Citizen Category")

"""
Output
Enter age: 20
It is an adult

Enter age: 19
It is a Teen

Enter age: 34
It is an adult

Enter age: 45
It is an adult

Enter age: 2
It is an infant

Enter age: 90
Sr. Citizen Category