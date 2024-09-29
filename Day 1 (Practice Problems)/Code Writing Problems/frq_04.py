
# Checking for even parity
total_sum = 0

for number in range(2, 201):
    # Check number is even
    if number % 2 == 0:
        total_sum += number

print(total_sum)

# Using step
total_sum = 0

for number in range(2, 201, 2):
    total_sum += number

print(total_sum)