def mapper(func, *sequences):
    if len(sequences)>1:
        while True:
            list.append(func(sequences[0][0],sequences[0][0],))
    return list

def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = mapper(square, numbers)

print(squared_numbers)