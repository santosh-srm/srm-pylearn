  
"""Print first n even numbers."""

def print_even_Nos(n):
    """Funtion to print even nos."""
    print(f"Even numbers under {n}")
    for i in range (0,n,2):
        print(i)

def main():
    print_even_Nos(13)
    print_even_Nos(21)
    print("End of Program")

main()
"""
Output
Even numbers under 13
0
2
4
6
8
10
12
Even numbers under 21
0
2
4
6
8
10
12
14
16
18
20
End of Program
"""