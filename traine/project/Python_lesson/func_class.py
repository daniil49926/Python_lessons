import time


class Multiplier:

    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x ** self.n


time_start = time.time()
my_num = Multiplier(100000)
print(my_num(222))
print("--- %s second ---" % (time.time() - time_start))