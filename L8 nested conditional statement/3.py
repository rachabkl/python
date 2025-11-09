print ("Select your ride: ")
print ("1. Bike")
print ("2. Car")

choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    print ("What type of bike? ")
    print ("1. Sports Bike\n")
    print ("2. Scooter Bike\n")

    choice2 = int(input("Enter your choice (1 or 2): "))
    if choice2 == 1:
        print ("You have selected Sports Bike")     
    else: 
        print ("You have selected Scooter Bike")
elif choice == 2:
    print ("What type of car? ")
    print ("1. Sedan Car\n")
    print ("2. SUV Car\n")

    choice3 = int(input("Enter your choice (1 or 2): "))
    if choice3 == 1:
        print ("You have selected Sedan Car")     
    else: 
        print ("You have selected SUV Car")