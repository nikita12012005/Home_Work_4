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

