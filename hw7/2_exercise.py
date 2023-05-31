def my_filter(function, iterable):
    return (item for item in iterable if function(item))
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = my_filter(is_even, numbers)

print(list(filtered_numbers))
