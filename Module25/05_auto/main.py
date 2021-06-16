import math


class Car:
    def __init__(self, x, y, angle):
        self.__x = x
        self.__y = y
        self.__angle = angle

    def drive(self, distance):
        self.__x = round(self.__x + (math.cos(math.radians(self.__angle)) * distance), 2)
        self.__y = round(self.__y + (math.sin(math.radians(self.__angle)) * distance), 2)

    def get_x_y(self):
        return "({} , {})".format(
            self.__x, self.__y
        )

    def turn(self, angle):
        self.__angle += angle


class Bus(Car):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.__passenger = 0
        self.__money = 0

    def come_in(self, passenger):
        self.__passenger += passenger

    def come_out(self, passenger):
        self.__passenger -= passenger

    def drive(self, distance):
        super().drive(distance)
        self.__money += self.__passenger * distance * 5

    def get_money(self):
        return self.__money


bus = Bus(0, 0, 90)
bus.come_in(2)
bus.drive(5)
print(bus.get_x_y())
bus.come_out(1)
bus.turn(-90)
bus.drive(5)
print(bus.get_x_y())
print(bus.get_money())

# зачёт! 🚀
