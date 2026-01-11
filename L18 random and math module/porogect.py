import math

angle_deg = float(input("Enter the angle in degrees: "))
angle_rad = math.radians(angle_deg)
sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)
print("Sin =", sin_value)
print("Cos =", cos_value)
print("Tan =", tan_value)
