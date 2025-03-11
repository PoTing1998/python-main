# self mode iterator


class MyIterator:
    def __init__(self, max):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            result = self.n
            self.n += 1
            return result
        else:
            raise StopIteration
        
my_iter = MyIterator(3)

for i in my_iter:
    print(i)
    