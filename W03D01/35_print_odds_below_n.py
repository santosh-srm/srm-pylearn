"""Print Odd Nos. Below the given number"""

def print_odd(n):
    """Print odd numbers below the given number"""
    print(f'---Print Odd Numbers below {n}---')
    print("*********************************")
    for i in range(1,n,2):
     
        print(i)
     

def main():
    print_odd(10)
    print("\n")  
    print_odd(15)
    print("End of Program")
main()

"""Output
---Print Odd Numbers below 10---
*********************************
1
3
5
7
9


---Print Odd Numbers below 15---
*********************************
1
3
5
7
9
11
13
End of Program
"""