def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def modules(x,y):
    return x % y
def floor(x,y):
    return x // y

print("Enter your choice: ")
print("a. Add\n b. Subtract\n c. Multiply\n d. Divide\n e. Modules\n f. Floor Division") 
choice = input().lower().strip()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "a":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == "b": 
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice == "c":
    print(num1,"*",num2,"=",multiply(num1,num2))    
elif choice == "d":
    print(num1,"/",num2,"=",divide(num1,num2))
elif choice == "e":
    print(num1,"%",num2,"=",modules(num1,num2))
elif choice == "f":
    print(num1,"//",num2,"=",floor(num1,num2))
else:
    print("Invalid input")