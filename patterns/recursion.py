import sys


#sys.setrecursionlimit(3000)


def add_numbers(n: int) -> int:
    # Set the base case 
    if n >= 200:
        return 0

    else:
        print(f"Adding {n}")
        return n + add_numbers(n+1)


# Factorial of a number using Recursion

def fact(n: int) -> int:
    # base case
    if n == 0:
        return 1
    print(f"factorial of {n} called")
    return n * fact(n-1)

if __name__ == "__main__":
    # n = int(input("Enter a number to compute factorial: "))
    # print(f"{n}! is {fact(n)}")
    add_numbers(10)