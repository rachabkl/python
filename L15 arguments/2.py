def factorial(x):
    """This is a recursive function to find factorial of an integer"""
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print(f"The factorial of :{factorial(0)}")
print(f"The factorial of :{factorial(1)}")
print(f"The factorial of :{factorial(4)}")
print(f"The factorial of :{factorial(5)}")
print(f"The factorial of :{factorial(10)}")