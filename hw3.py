# 1_exercise
odd = [1, 3, 5, 7]
even = [2, 4, 6, 8]

for index, value in zip(odd, even):
    print(f'index: {index}, value: {value}')

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