"""23_eligibility_form.py."""

print("----Program to find eligibility----")

name = input("Enter candidate name: ")
age = int(input("Enter candidate age: "))

if (age > 18):
    print(f"{name} is eligible for enrollment")
else:
    print(f"{name} is still not eligible. Try next time")

"""
Enter candidate name: Sam
Enter candidate age: 14
Sam is still not eligible. Try next time

----Program to find eligibility----
Enter candidate name: Sandy
Enter candidate age: 21
Sandy is eligible for enrollment
""""