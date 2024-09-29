# Input
number = input("Enter a phone number in this format XXX-XXXXXXX: ")

# Processing
front = number[:3]
letters = number[4:]

# Convert letters to numbers
numbers = []
phone = ["ABC", "DEF", "GHI", "JKL", "MNO",
         "PQRS", "TUV", "WXYZ"]
# For each letter...
for letter in letters:
    # ...check to see if belongs in letter group
    for group_index in range(len(phone)):
        if letter in phone[group_index]:
            numbers.append(str(group_index + 2))

# Put everything together
middle = "".join(numbers[:3])
end = "".join(numbers[3:])
phone_number = f"{front}-{middle}-{end}"

# Output
print(f"{number} is equivalent to {phone_number}")