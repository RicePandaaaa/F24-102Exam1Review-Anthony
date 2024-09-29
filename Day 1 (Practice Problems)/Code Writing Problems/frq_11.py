# Table formatting
print("-----------------------------------------------")
print("Integer Multiples")
print("-----------------------------------------------")

# Make table
for n in range(2, 6):
    multiples = []

    for factor in range(1, 11):
        multiples.append(str(n * factor))

    multiples_str = ", ".join(multiples)
    # Output
    print(f"{n}\t{multiples_str}")

print("-----------------------------------------------")