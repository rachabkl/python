units = int(input("Enter the number of units consumed: "))
if units < 50 :
    amount = units * 2.5
    surcharge = 25
elif units < 150 :
    amount = (50 * 2.5) + (units - 50) * 5
    surcharge = 50
elif units < 250:
    amount = (50 * 2.5) + (100 * 5) + (units - 150) * 6.2
    surcharge = 75
else:
    amount = (50 * 2.5) + (100 * 5) + (100 * 6.2) + (units - 250) * 7.5
    surcharge = 100
total_bill = amount + surcharge
print(f"The total electricity bill is: {total_bill}")