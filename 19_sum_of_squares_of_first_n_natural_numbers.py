"""19_sum_of_squares_of_first_n_natural_numbers.py

Formula=[n(n+1)(2n+1)]/6
"""
print("---- Sum of Squares of first n Natural numbers ----")

print("Enter the Natural Number: ")
n=int(input(""))
sumofsquares=(n*(n+1)*(2*n+1))//6

print(f"Sum of Squares of first {n} Natural numbers is: {sumofsquares}")

"""
Output

Enter the Natural Number:
4
Sum of Squares of first 4 Natural numbers is: 30
"""
#(1*1)+(2*2)+(3*3)+(4*4)