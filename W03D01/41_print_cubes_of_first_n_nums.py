"""Program to print cubes of first n even numbers"""

def print_cubes(n):
    """Function to print cubes of first n even numbers"""
    print("This function prints cubes of even numbers below {n}")
    for i in range(1,n):
        if (i%2==0):
            print(f"Cube of {i} is {i*i*i}")

def main():
    print_cubes(15)
    print_cubes(25)


main()

"""Output

c:/akademize/W01D01/srm-pylearn/W03D01/41_print_cubes_of_first_n_nums.py
This function prints cubes of even numbers below {n}
Cube of 2 is 8
Cube of 4 is 64
Cube of 6 is 216
Cube of 8 is 512
Cube of 10 is 1000
Cube of 12 is 1728
Cube of 14 is 2744
This function prints cubes of even numbers below {n}
Cube of 2 is 8
Cube of 4 is 64
Cube of 6 is 216
Cube of 8 is 512
Cube of 10 is 1000
Cube of 12 is 1728
Cube of 14 is 2744
Cube of 16 is 4096
Cube of 18 is 5832
Cube of 20 is 8000
Cube of 22 is 10648
Cube of 24 is 13824

"""