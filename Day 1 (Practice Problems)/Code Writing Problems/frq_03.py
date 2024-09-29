roster = [['123004567', ['Joe', 'Aggie', 'ENGE', 3.50]], 
          ['123004568', ['Jake', 'Green', 'OCEN', 3.75]], 
          ['123004569', ['Jill', 'Apple', 'ENGR', 3.25]]]

# Input
uin = input("Enter a UIN: ")

# Validate UIN
for row in roster:
    if uin == row[0]:
        data = row[1]

        # Get my data fields
        first = data[0]
        last = data[1]
        major = data[2]
        gpa = data[3]

        # Output
        print(f"{first} {last}: {major}, {gpa:.2f}")

        break