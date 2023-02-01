class OddEvenNumber:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.limit:
            number = self.n
            self.n += 1
            if number % 2:
                return number
            return -1*number


odd_even = OddEvenNumber(20)
iterator = iter(odd_even)
k = 0
while k < 20:
    print(next(iterator))
    k += 1
