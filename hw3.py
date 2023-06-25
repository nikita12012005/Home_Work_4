elements = [1, 2, 3, 4, 5, 6, 7, 8]

odd_index_elements = []
even_index_elements = []

for index, value in enumerate(elements):
    if index % 2 == 0:
        even_index_elements.append((index, value))
    else:
        odd_index_elements.append((index, value))

print("Elements with odd indices:")
for item in odd_index_elements:
    print(item)

print("\nElements with even indices:")
for item in even_index_elements:
    print(item)

#2_exercise
multiplication_way_one= 2*2
print(multiplication_way_one)
multiplication_way_two= 2**2
print(multiplication_way_two)
division_way_one= 2/2
print(division_way_one)
division_way_two = 2//2
print(division_way_two)

#3_exercise
friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]
for friend, enemie in zip(friends, enemies):
    if friend== enemie:
        print(f'{friend} we are not friends anymore')
    elif friend!=enemie and friend!='James':
        print(f'{friend} we are the best friends')


