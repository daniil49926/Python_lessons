from collections.abc import Iterable


class Square:
    def __init__(self, num: int) -> None:
        self.num = num
        self.start = 0

    def __iter__(self) -> iter:
        self.start = 0
        return self

    def __next__(self) -> int:
        self.start += 1
        if self.num >= self.start:
            return self.start ** 2
        else:
            raise StopIteration


def square(stop_num: int) -> Iterable[int]:
    start_num = 1
    while start_num <= stop_num:
        yield start_num ** 2
        start_num += 1


input_num = int(input())

v_1 = Square(input_num)
v_2 = square(input_num)
v_3 = (num ** 2 for num in range(1, input_num + 1))

for i in v_1:
    print(i)

for i in v_2:
    print(i)

for i in v_3:
    print(i)

# зачёт! 🚀
