


def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in input_string if char not in vowels)
print(remove_vowels("Hello, World!"))


