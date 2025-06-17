import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Read number from command-line
if len(sys.argv) != 2:
    print("Usage: python prime_check.py <number>")
else:
    try:
        num = int(sys.argv[1])
        if is_prime(num):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")
    except ValueError:
        print("Please provide a valid integer.")
