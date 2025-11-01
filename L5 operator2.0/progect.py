# Program to check wether a character is a digit, an alphabet or neither

# Ask the user to enter a character
char = input("Enter a character: ")

# Check if the character is a digit
if "0" <= char <= "9":
    print(f"{char} is a digit.")

# Check if the character is an alphabet in uppercase or lowercase
elif ("A" <= char <= "Z") or ("a" <= char <= "z"):
    print(f"{char} is an alphabet.")

# If it's neither a digit nor an alphabet
else:
    print(f"{char} is neither a digit nor an alphabet.")