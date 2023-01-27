def check_argument(func):
    def wrapper(lst):
        if type(lst) == list:
            return func(lst)
        else:
            print("Please send only list")

    return wrapper


@check_argument
def sum_index(lst):
    return sum(range(0, len(lst)))


print(sum_index([1, 2, 3, 4]))
