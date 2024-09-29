# Input
n = int(input("Enter a positive integer: "))

print(f"Here is the Fibonacci sequence up to {n}:")

# Output
print("0, 1, ", end="")

# Variables to hold sequence
a = 0
b = 1
c = a + b

while c <= n:
    print(c, end="")

    # Continue the sequence
    a = b
    b = c
    c = a + b

    # Check if there is a next term
    if c <= n:
        print(", ", end="")