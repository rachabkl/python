st = input("Enter your ownwords: ")
ch = input("Enter a character to find frequency: ")
i = 0
count = 0
while i < len(st):
    if (st[i] == ch):
       count = count + 1
    i += 1
print(f"The frequency of {ch} in the given string is: {count}")
