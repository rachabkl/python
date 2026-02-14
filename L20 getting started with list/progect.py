def square_numbers(start, end):
    squares = []

    # Calcul des carrés
    for i in range(start, end + 1):
        squares.append(i ** 2)

    # Filtrer pairs et impairs
    even_squares = []
    odd_squares = []

    for num in squares:
        if num % 2 == 0:
            even_squares.append(num)
        else:
            odd_squares.append(num)

    print("All square values:", squares)
    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)


# Exemple d'utilisation
square_numbers(1, 10)
