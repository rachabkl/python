# Given tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

# Function to calculate product of a tuple
def tuple_product(t):
    product = 1
    for num in t:
        product *= num
    return product

# Calculating products
result1 = tuple_product(tup1)
result2 = tuple_product(tup2)

# Printing results
print("Product of tup1:", result1)
print("Product of tup2:", result2)
