# Inputs
items = []

print("Enter 5 items and their cost")
for i in range(5):
    item = input(f"Item {i+1}: ")
    items.append(item)

budget = float(input("How much money to you have? "))

# Go through each item
affordable_items = []
for item in items:
    parts = item.split(" ")
    item_name = parts[:-1]
    item_name = " ".join(item_name)
    cost = float(parts[-1])

    # Check if user can afford
    if budget >= cost:
        affordable_items.append(item_name)

# Format
print("You can afford ", end="")

if len(affordable_items) == 1:
    print(affordable_items[0])
elif len(affordable_items) == 2:
    print(f"{affordable_items[0]} or {affordable_items[1]}")
else:
    for item in affordable_items[:-1]:
        print(item, end=", ")
    print(f"or {affordable_items[-1]}")
