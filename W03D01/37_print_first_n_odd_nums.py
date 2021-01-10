"""Print Odd Nos. Below the given number"""

def print_odd_Nos(m,n):
    """Print odd numbers below the given number"""
    print(f'---Print Odd Numbers between {m} & {n}---')
    print("*********************************")
    for i in range(m,n):
        if (i%2 != 0):
            print(i)
     

def main():
    print_odd_Nos(20,35)
    print_odd_Nos(11,30)
    print("End of Program")
main()

"""
Output
---Print Odd Numbers between 20 & 35---
*********************************
21
23
25
29
31
33


---Print Odd Numbers between 11 & 30---
*********************************
11
13
15
17
19
21
23
25
27
29
End of Program
"""