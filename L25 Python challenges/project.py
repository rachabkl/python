import random
import string

# Ask the user for password length
length = int(input("Enter password length: "))

# Combine lowercase, uppercase, and digits
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Generate random password
password = ''.join(random.choice(characters) for _ in range(length))

# Shuffle the password (optional)
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

# Display the password
print("Generated Password:", password)