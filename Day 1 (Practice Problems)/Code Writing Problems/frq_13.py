# Input
number = input("Enter an integer with 10+ digits: ")
digit = input("Enter a digit: ")

"""
# Loop to exclude
new_num = ""
for n in number:
    # digit found, skip
    if n == digit:
        continue

    # otherwise, add
    new_num += n
"""

# GENIUS USAGE OF SPLIT + JOIN!!!
groups = number.split(digit)
new_num = "".join(groups)

# Output
print(f"New number is {new_num}")