actual_cost = float(input("Enter the Actual prie: "))
sale_cost = float(input("Enter the Sales price: "))

if sale_cost > actual_cost :
    amount = sale_cost - actual_cost
    print(f"Total profit = {amount}")
else:
    amount = sale_cost - actual_cost
    print(f"Oops!\nTotal loss = {amount}")
