a = 12 
b = 3 
c = 4 
d = 9 
answer = b**c + d/ b*c + a
print(f"The value of the expression is: {answer}")

n1 = int(input("\nEnter numerator: "))
n2 = int(input("Enter denominator: "))
if n1%n2 == 0:
    print(str(n1) + " is completely divisible by " + str(n2))
else:
    print(str(n1) + " is not completely divisible by " + str(n2))