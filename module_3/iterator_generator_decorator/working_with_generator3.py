def twice_add(a: int, b: int):
    n = 0
    while n >= 0:
        yield 2 * (a + b)
        n += 1


add_ = twice_add(2, 3)
print(next(add_))
print(next(add_))
print(next(add_))
