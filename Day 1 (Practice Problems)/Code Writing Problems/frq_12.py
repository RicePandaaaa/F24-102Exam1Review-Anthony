"""
Method 1: str -> list of str -> add ints
# Get input
integer = input("Enter a positive integer: ")

# Break into digits
digits = list(integer)

# Add
total = 0
for digit in digits:
    total += int(digit)

print(f"Sum of the digits: {total}")
"""

# Method 2: Modulus + Division
# Get input
number = int(input("Enter a positive integer: "))

# Add
total = 0
while number > 0:
    digit = number % 10
    total += digit
    number = number // 10

print(f"Sum of the digits: {total}")

