# a->e pyramid
letters = ["a", "b", "c", "d", "e"]

for index in range(len(letters)):
    letter = letters[index]
    quantity = index + 1
    # Can replace loop with print(letter * quantity) and discard print()
    for _ in range(quantity):
        print(letter, end="")
    print()

# > pyramid
quantity = 1
change = 1
for i in range(5):
    print(">" * quantity)
    if quantity == 3:
        change = -1
    quantity += change

# * pyramid
quantity = 3
change = -1
for i in range(5):
    print("*" * quantity)
    if quantity == 1:
        change = 1
    quantity += change

# upside down pyramid
letter = "o"
for i in range(5):
    #print(f"{" " * i}{letter * (5 - i)}")
    print(f"{letter * (5 - i):>5}")

# combined pyramids
letter = "x"
for i in range(5):
    #print(f"{" " * i}{letter * (5 - i)}")
    print(f"{letter * (4 - i):o<5}")