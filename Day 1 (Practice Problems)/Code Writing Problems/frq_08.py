# Input
number = int(input("Enter an integer between 100 and 1000000, inclusive: "))

# Range check
if not (100 <= number <= 1000000):
    print("Wrong input!")

else:
    # Grab last two digits
    number = str(number)
    left = int(number[len(number)-2])
    right = int(number[len(number)-1])

    print(left, right)

    # Odd, even check
    if (left % 2 == 0) and (right % 2 == 0):
        print("Both even!")
        print(f"Sum = {left + right}")

    elif (left % 2 == 1) and (right % 2 == 1):
        print("Both odd!")
        print(f"Product = {left * right}")

    else:
        print("One odd, one even.")