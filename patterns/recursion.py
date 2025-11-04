# Simple Recursive funtion to demonstrate recursion

# TODO: Fix RecursionError: maximum recursion depth exceeded
def add_numbers(n):
    # Set the base case 
    if n == 1000:
        return n
    else:
        return n + add_numbers(n+500)


# Factorial of a number using Recursion

def fact(n):
    # base case
    if n == 0:
        return 1
    print(f"factorial of {n} called")
    return n * fact(n-1)

if __name__ == "__main__":
    n = int(input("Enter a number to compute factorial: "))
    print(f"{n}! is {fact(n)}")