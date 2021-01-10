"""Print a multiplication table."""

def main():
    """Printing Multiplication Table"""
    print_table(2)
    print_table(7)
    print_table(13)

def print_table(n):
    """Print nth Multiplication Table"""
    print(f"Table {n}")
    for i in range(1, 11):
        print(f'{n} * {i} = {n*i}')
    print("\n")

main()


""" Output
Table 2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20


Table 7
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70


Table 13
13 * 1 = 13
13 * 2 = 26
13 * 3 = 39
13 * 4 = 52
13 * 5 = 65
13 * 6 = 78
13 * 7 = 91
13 * 8 = 104
13 * 9 = 117
13 * 10 = 130

"""
