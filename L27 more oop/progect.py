# Import math module
import math

# Create class
class Circle:

    # Constructor
    def __init__(self, radius):
        self.radius = radius

    # Function to calculate area
    def area(self):
        return math.pi * self.radius * self.radius

    # Function to calculate perimeter
    def perimeter(self):
        return 2 * math.pi * self.radius


# Take input from user
r = float(input("Enter the radius: "))

# Create object
c1 = Circle(r)

# Display results
print("Area of circle =", c1.area())
print("Perimeter of circle =", c1.perimeter())