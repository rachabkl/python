# Ask the user to enter a number
n = int(input("Enter a number: "))

# Create a list of odd numbers less than n
odd_numbers = [i for i in range(n) if i % 2 != 0]

print("Odd numbers:", odd_numbers)


# Create a list of fruits
fruits = ["apple", "banana", "cherry", "orange"]

# Capitalize the first letter of each fruit
updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Updated fruits:", updated_fruits)
