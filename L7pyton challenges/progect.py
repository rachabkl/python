# Program to swap three numbers 
# Getting input from the user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): ")) 
c = int(input("Enter third number (c): "))  

print(f"\nBefore swapping: a = {a}, b = {b}, c = {c}")

# Swapping logic
temp = a
a = b
b = c
c = temp
print(f"\nAfter swapping: a = {a}, b = {b}, c = {c}")