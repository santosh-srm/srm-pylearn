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