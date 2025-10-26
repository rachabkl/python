height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / ((height / 100) ** 2)

print("Your BMI is:", BMI)
if BMI < 18.5:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healty.")
elif BMI <= 29.9:
    print("You are overweight.")
elif BMI <= 34.9:
    print("You are obese class I.")
elif BMI <= 39.9:
    print("You are obese class II.")
else:
    print("You are obese class III.")