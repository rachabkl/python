from abc import ABC, abstractmethod

# Abstract class
class Device(ABC):

    @abstractmethod
    def turn_on(self):
        pass


# Light class
class Light(Device):

    def turn_on(self):
        print("The light is on.")


# Fan class
class Fan(Device):

    def turn_on(self):
        print("The fan is on.")


# Speaker class
class Speaker(Device):

    def turn_on(self):
        print("The speaker is on.")


# Create objects
light = Light()
fan = Fan()
speaker = Speaker()

# Put them in a list
devices = [light, fan, speaker]

# Polymorphism
for device in devices:
    device.turn_on()