number = int(input("Enter a number: "))

count = 0
temp = number
while temp > 0:
    temp = temp // 10
    count = count + 1
print(f"The number of digits in {number} is {count}.")