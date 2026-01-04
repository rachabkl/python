try:
    num,num1 = eval(input("Enter two numbers separated by a comma:"))
    result = num/num1
    print("Result is:",result)
except ZeroDivisionError :
    print("OOO..oops!\nDivision with zero is an Error!!!")
except SyntaxError :
    print("Coma is missing. Enter numbers separated by comma like this 1,2")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")