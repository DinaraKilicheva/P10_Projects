def only_even_parameters(func):
    def wrapper(*args):
        if sum([i % 2 for i in args]):
            return "Please multiply only even  numbers"
        return func(*args)

    return wrapper


@only_even_parameters
def multiply(a, b):
    return a + b


@only_even_parameters
def multiply_(a, b, c, d):
    return a * b * c * d


print(multiply(6, 4))
print(multiply_(2, 1, 3, 4))
