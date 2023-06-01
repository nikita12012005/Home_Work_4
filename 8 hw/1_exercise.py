def log_function_name(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        return func(*args, **kwargs)
    return wrapper
def summation(a, b):
    return a + b
def multiplication(a, b):
    return a * b
result_1 = summation(3, 4)
print("Result:", result_1)
result_2 = multiplication(2, 5)
print("Result:", result_2)