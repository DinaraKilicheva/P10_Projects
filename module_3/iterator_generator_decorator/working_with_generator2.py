def get_next_prime():
    for element in range(3, 1000):
        bool_ = True
        for i in range(2, element):
            if element % i == 0:
                bool_ = False
        if bool_:
            yield element


prime_generator = get_next_prime()
print(next(prime_generator))
print(next(prime_generator))
print(next(prime_generator))
print(next(prime_generator))
