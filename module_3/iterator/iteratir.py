class Num:
    def __init__(self, limit=20):
        self.limit = limit

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.limit:
            odd_numbers = self.n + 2
            self.n+=1
            return odd_numbers

        else:
            raise StopIteration


numbers = Num()
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
