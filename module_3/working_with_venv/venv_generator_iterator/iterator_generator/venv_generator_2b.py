def gen_func(n):
    for i in range(1, n + 1):
        if i % 2:
            yield i
        else:
            yield -1 * i


gen_fun = gen_func(20)
k = 0
while k < 20:
    print(next(gen_fun))
    k += 1
