import math



def square(side_length):

    perimeter = 4 * side_length
    area = side_length ** 2
    diagonal = math.sqrt(2) * side_length

    return (perimeter, area, diagonal)
perimeter, area, diagonal = square(10)
print("Perimeter:", perimeter)
print("Area:", area)
print("Diagonal:", diagonal)

