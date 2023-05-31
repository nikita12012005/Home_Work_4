def my_all(iterable):
    for item in iterable:
        if not item:
            return False
    return True
numbers = [2, 4, 6, 8, 10]
are_all_even = my_all([num % 2 == 0 for num in numbers])
print(are_all_even)

mixed_list = [1, 3, 5, 7, 10]
are_all_even = my_all([num % 2 == 0 for num in mixed_list])
print(are_all_even)
