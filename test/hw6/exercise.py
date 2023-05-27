import math
import re
#1_exercise
def arithmetic(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        raise ValueError("Not known operation: {}".format(operation))
#2_exercise


def square(side_length):

    perimeter = 4 * side_length
    area = side_length ** 2
    diagonal = math.sqrt(2) * side_length

    return (perimeter, area, diagonal)
perimeter, area, diagonal = square(10)
print("Perimeter:", perimeter)
print("Area:", area)
print("Diagonal:", diagonal)
#3_exercise
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
print(is_prime(11))
print(is_prime(121))
#4_exrcise
def remove_numbers_from_file(file_path):
    output_file_path = "output.txt"

    with open(file_path, "r") as input_file, open(output_file_path, "w") as output_file:
        for line in input_file:
            line_without_numbers = re.sub(r'\d+', '', line)
            output_file.write(line_without_numbers)

    print("Numbers removed and saved to '{}'".format(output_file_path))
#6_exercise
def calculate_sum(*args):
    return sum(args)
print(calculate_sum(1, 2, 3, 4, 5))

#7_exercise
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in input_string if char not in vowels)
print(remove_vowels("Hello, World!"))
#8_exercise
def display_box(width: int, height: int, character: str = "*"):
    print(character * width)


    for _ in range(height - 2):
        print(character + " " * (width - 2) + character)


    if height > 1:
        print(character * width)
display_box(10, 9, 'x')