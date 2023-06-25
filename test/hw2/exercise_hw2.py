#2_exercise
eleks={'Kate', 'Vlad', 'Nikita', 'Kolia'}
toshiba={'Nikita', 'Kate', 'Vlad', 'Max'}
result= eleks.union(toshiba)
print(result)
#3_exrcise
casino_blacklist={'Nikita Kruk', 'Anna Chupryna', 'Oleksandr Karasov'}
poker_blacklist={'Misha Sutiahin','Anna Chupryna', 'Nikita Kruk'}
alcohol_blacklist={'Yuliia Onyshchenko-Mussa', 'Iryna Kyshmar', 'Anna Chupryna'}
casino_and_poker= casino_blacklist.intersection(poker_blacklist)
blacklist= alcohol_blacklist.intersection(casino_and_poker)
print(blacklist)
#4_exercise
omnivores = ["John", "Mary", "Peter", "Sarah"]
vegetarians = ["Alice", "Bob", "Emma", "Tom"]
guests_eating_vegetables = []
for guest in omnivores:
    guests_eating_vegetables.append(guest)

for guest in vegetarians:
    if guest not in guests_eating_vegetables:
        guests_eating_vegetables.append(guest)

print("Guests who can eat vegetables and herbs:")
for guest in guests_eating_vegetables:
    print(guest)
#5_exercise
vip={'Bohdan', 'Dima', 'Vlad'}
common=['Kolia', 'Vasia', 'Den', 'New_name', 'New_name_2']
common.extend(['New_name', 'New_name_2'])
print(vip)
print(common)
#6_exercise
people = ["John Dow", "John Dow", "Marta Dow", "Alice Smith", "Bob Johnson", "Alice Smith"]

non_duplicate_names = []

for person in people:
    if person not in non_duplicate_names:
        non_duplicate_names.append(person)

print("Non-duplicate names:")
for name in non_duplicate_names:
    print(name)

