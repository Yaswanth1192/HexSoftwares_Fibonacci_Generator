# Fibonacci Series Program
# This program prints the Fibonacci series up to a given number of terms.

# Ask the user how many terms they want
n_terms = int(input("Enter the number of terms: "))

# First two terms of the Fibonacci sequence
a = 0
b = 1

# Check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence up to", n_terms, "term:")
    print(a)
else:
    print("Fibonacci sequence:")
    print(a, b, end=" ")
    # Loop to generate the remaining terms
    for i in range(2, n_terms):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
