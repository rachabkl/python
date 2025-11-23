decimal = float(input("Enter a decimal number: "))
temp = decimal
binary = ""
while temp > 0:
    remainder = temp % 2
    binary = str(remainder) + binary
    temp = temp // 2
print(f"The binary representation of {decimal} is {binary}.")