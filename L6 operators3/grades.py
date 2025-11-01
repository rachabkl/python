print (" Enter the marks obteined in 5 subjects ")
m1 = int( input("mark 1: "))
m2 = int( input("mark 2: "))
m3 = int( input("mark 3: "))
m4 = int( input("mark 4: "))
m5 = int( input("mark 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5
print(f"Total marks = {total}")
print(f"Average marks = {average}")

if average >= 91 and average <= 100:
    print("Grade A+")
elif average >= 81 and average <= 91:
    print("Grade A")
elif average >= 71 and average <= 81:
    print("Grade B+")
elif average >= 61 and average <= 71:
    print("Grade B")
elif average >= 51 and average <= 61:
    print("Grade C+")
elif average >= 41 and average <= 51:
    print("Grade C")
elif average >= 31 and average <= 41:
    print("Grade D")
elif average >= 21 and average <= 31:
    print("Grade E")
elif average >= 0 and average <= 21:
    print("Grade F")
else:
    print("Invalid Input")