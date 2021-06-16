from math import sqrt


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r
        self.pi = 3.14159265359

    def square(self):
        return self.pi * pow(self.r, 2)

    def perimeter(self):
        return 2 * self.pi * self.r

    def buf(self, k):
        self.r = self.r * k

    def intersection(self, obj):
        if sqrt(pow(self.x - obj.x, 2) + (pow(self.y - obj.y, 2))) > (self.r + obj.r):
            print("Пересечений нет")
        else:
            print("Пересечения есть")


c1 = Circle(x=1, y=1, r=1)
print(c1.square())
print(c1.perimeter())
c1.buf(2)
print(c1.square())
c2 = Circle(x=2, y=2, r=1)
c3 = Circle(x=-10, y=-5, r=1)
c1.intersection(c2)
c1.intersection(c3)

# зачёт! 🚀
