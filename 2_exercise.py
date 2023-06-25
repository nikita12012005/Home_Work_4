#2_exercise
def camel_to_snake(variable_name):
    result = ''
    for i, char in enumerate(variable_name):
        if char.isupper() and i > 0:
            result += '_'
        result += char.lower()
    return result

camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = [camel_to_snake(variable_name) for variable_name in camel_case_list]

print(snake_case_list)
