def get_next_multiple(a):
    n = 1
    while n < 10:
        yield n * a
        n += 1


get_multiple_two = get_next_multiple(2)
print(next(get_multiple_two))
print(next(get_multiple_two))
print(next(get_multiple_two))
print(next(get_multiple_two))
