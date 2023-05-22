import os
import random
#1_exrcise

my_list = []
for _ in range(100):
    left_operand = random.randint(1, 100)
    right_operand = random.randint(1, 100)
    operation = random.randint(1, 3)
    my_list.append((left_operand, right_operand, operation))

os.makedirs('test/data', exist_ok=True)
file = 'test/data/tuple_data.txt'
with open(file, 'w') as file:
    for tuple_data in my_list:
        line = ' '.join(str(element) for element in tuple_data)
        file.write(line + '\n')

print(f"Data saved to {file}")
#2_exercise
filename = 'test/data/tuple_data.txt'
with open(filename, 'r') as file:
    for line in file:
        elements = line.strip().split()
        left_operand = int(elements[0])
        right_operand = int(elements[1])
        operation = int(elements[2])

        result = None
        if operation == 1:
            result = left_operand + right_operand
        elif operation == 2:
            result = left_operand - right_operand
        elif operation == 3:
            result = left_operand * right_operand

        print(result)
#3_exercise
filename = 'text.txt'


letter_counts = {}


with open(filename, 'r') as file:
    for line in file:

        line = line.strip().lower()


        for char in line:

            if char.isalpha():

                letter_counts[char] = letter_counts.get(char, 0) + 1


for letter, count in letter_counts.items():
    print(f"{letter}: {count}")

