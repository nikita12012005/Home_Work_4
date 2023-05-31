def my_max(iterable, amount=1):
    sorted_items = sorted(iterable, reverse=True)
    return sorted_items[:amount]


def my_min(iterable, amount=1):
    sorted_items = sorted(iterable)
    return sorted_items[:amount]

numbers = [5, 2, 8, 1, 9, 3, 7, 6, 4]
max_values = my_max(numbers)
min_values = my_min(numbers)
two_max_values = my_max(numbers, amount=2)

print(max_values)
print(min_values)
print(two_max_values)
