rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Print spaces first
    print(" " * (rows - i), end="")
    # Then print stars
    print("*" * i)
