"""
TASK01
"""


class Family:
    def __init__(self):
        self.dad = "Игорь"
        self.mom = "Марина"
        self.son = "Даниил"
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i == 1:
            return f"Мама - {self.mom}"
        if self.i == 2:
            return f"Папа - {self.dad}"
        if self.i == 3:
            return f"Я - {self.son}"
        if self.i == 4:
            return f"Счастливая семью!"
        raise StopIteration()


my_family = Family()
for i in my_family:
    print(i)


"""
TASK02
"""


class Fibonacci:
    def __init__(self, stop):
        self.start = 0
        self.start_plus = 1
        self.stop = stop
        self.i = 2
        self.result = 0

    def __iter__(self):
        self.i = 2
        self.result = 0
        return self

    def __next__(self):
        if self.i < self.stop:
            self.i += 1
            self.start, self.start_plus = self.start_plus, self.start + self.start_plus
            return self.start_plus
        raise StopIteration()

    @staticmethod
    def fib(stop):
        if stop == 0:
            return print(0)
        ret_res = 1
        fib = Fibonacci(stop)
        for step in fib:
            ret_res += step
        print(ret_res)


Fibonacci.fib(5)

my_fib = Fibonacci(1000)
print(13 in my_fib)



