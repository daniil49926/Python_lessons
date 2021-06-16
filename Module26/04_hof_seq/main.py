from collections.abc import Iterable


class QHofstadter:
    def __init__(self, n: list, limit: int) -> None:
        self.n = n[:]
        self.limit = limit

    def __iter__(self) -> iter:
        return self

    def __next__(self) -> Iterable[int]:
        try:
            if self.limit > 0:
                q = self.n[-self.n[-1]] + self.n[-self.n[-2]]
                self.n.append(q)
                self.limit -= 1
                return q
            else:
                raise StopIteration
        except IndexError:
            raise StopIteration


my_hof = QHofstadter([1, 1], limit=20)
for i in my_hof:
    print(i)