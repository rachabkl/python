base = int(input("Enter the base value: "))
power = int(input("Enter the power: "))
result = 1
for i in range(power):
    result = result * base
print(f"{base} to the power of {power} is {result}")