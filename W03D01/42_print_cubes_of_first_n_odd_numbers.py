"""Program to print cube of first n odd numbers"""

def print_cubes(n):
    """This function prints cube of odd numbers below given number"""
    print(f"This function prints cube of odd numbers below {n}")
    for i in range(1,n):
        if (i%2 != 0):
            print(f"The cube of {i} is {i*i*i}")

def main():
    print_cubes(20)
    print_cubes(25)

main()

"""Output
This function prints cube of odd numbers below 20
The cube of 1 is 1
The cube of 3 is 27
The cube of 5 is 125
The cube of 7 is 343
The cube of 9 is 729
The cube of 11 is 1331
The cube of 13 is 2197
The cube of 15 is 3375
The cube of 17 is 4913
The cube of 19 is 6859
This function prints cube of odd numbers below 25
The cube of 1 is 1
The cube of 3 is 27
The cube of 5 is 125
The cube of 7 is 343
The cube of 9 is 729
The cube of 11 is 1331
The cube of 13 is 2197
The cube of 15 is 3375
The cube of 17 is 4913
The cube of 19 is 6859
The cube of 21 is 9261
The cube of 23 is 12167
"""