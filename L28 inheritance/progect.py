# Parent class
class Vehicle:

    def __init__(self, capacity):
        self.capacity = capacity

    # Method to calculate fare
    def fare(self):
        return self.capacity * 100


# Child class
class Bus(Vehicle):

    # Override fare method
    def fare(self):
        total_fare = super().fare()
        final_fare = total_fare + (0.10 * total_fare)
        return final_fare


# Create object
school_bus = Bus(50)

# Display total fare
print("Total Bus Fare =", school_bus.fare())