#2_exercise
eleks={'Kate', 'Vlad', 'Nikita'}
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
casino_blacklist={'Nikita Kruk', 'Anna Chupryna', 'Oleksandr Karasov'}
poker_blacklist={'Misha Sutiahin','Anna Chupryna', 'Nikita Kruk'}
alcohol_blacklist={'Yuliia Onyshchenko-Mussa', 'Iryna Kyshmar', 'Anna Chupryna'}
casino_and_poker= casino_blacklist.intersection(poker_blacklist)
blacklist= alcohol_blacklist.intersection(casino_and_poker)
print(blacklist)
#5_exercise
