def  squares_of_even_elements():
    for number in range (0, 1000000001 , 2):
        yield number**2
for square in squares_of_even_elements():
    print(square)