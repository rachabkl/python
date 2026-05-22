# Create a class
class Dog:
    animal = "Dog"   # class variable

    # constructor
    def __init__(self, breed, colour):
        self.breed = breed      # instance variable
        self.colour = colour    # instance variable


# Create objects
dog1 = Dog("Labrador", "Black")
dog2 = Dog("German Shepherd", "Brown")

# Display details
print("Dog 1:")
print("Animal:", dog1.animal)
print("Breed:", dog1.breed)
print("Colour:", dog1.colour)

print("\nDog 2:")
print("Animal:", dog2.animal)
print("Breed:", dog2.breed)
print("Colour:", dog2.colour)