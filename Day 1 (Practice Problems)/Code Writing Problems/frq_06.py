# Input
ages = []

age = int(input("Enter an age: "))
while age >= 0:
    # Store the age
    ages.append(age)

    # Ask for another age
    age = int(input("Enter another age: "))

# Data
number = len(ages)
min_age = min(ages)
max_age = max(ages)

# Output
print("Number of people  Minimum age  Maximum age")
print(f"{number:<18}{min_age:<13}{max_age}")