import os
import random
#1_exrcise

my_list = []
for _ in range(100):
    left_operand = random.randint(1, 100)
    right_operand = random.randint(1, 100)
    operation = random.randint(1, 3)
    my_list.append((left_operand, right_operand, operation))

os.makedirs('../test/data', exist_ok=True)
file = '../test/data/tuple_data.txt'
with open(file, 'w') as file:
    for tuple_data in my_list:
        line = ' '.join(str(element) for element in tuple_data)
        file.write(line + '\n')

print(f"Data saved to {file}")



