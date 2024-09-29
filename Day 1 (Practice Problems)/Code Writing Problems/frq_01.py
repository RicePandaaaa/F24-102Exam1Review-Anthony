# Get user birthdays
user1 = input("User 1 please enter a birthday: ")
user2 = input("User 2 please enter a birthday: ")
user3 = input("User 3 please enter a birthday: ")
user4 = input("User 4 please enter a birthday: ")
user5 = input("User 5 please enter a birthday: ")

# For writing
"""
birthdays = []

for user_number in range(1,6):
    birthday = input(f"User {user_number} please enter a birthday: ")
    birthdays.append(birthday)

"""

birthdays = [user1, user2, user3, user4, user5]
birthday_floats = []
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# Convert text to float
for birthday in birthdays:
    month, day = birthday.split(" ")

    # Get the month number
    month_number = months.index(month) + 1

    # Get the day number
    day_number = day
    if int(day_number) < 10:
        day_number = "0" + day_number

    # Get the float
    full_date = float(f"{month_number}.{day_number}")
    
    # Store in list
    birthday_floats.append(full_date)

# Sort the dates
birthday_floats.sort()

# Dividing line
print("------------------------------------------------")

# Outputs
for birthday in birthday_floats:
    month, day = str(birthday).split(".")
    month_name = months[int(month) - 1]
    day_num = int(day)

    print(month_name, day_num)

