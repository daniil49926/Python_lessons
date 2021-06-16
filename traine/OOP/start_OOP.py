class Toyota:
    def __init__(self, speed, top_speed, color, price):
        self.speed = speed
        self.top_speed = top_speed
        self.color = color
        self.price = price

    def info(self):
        print(
            "Скорость в данный момент: {}\nМакс. скорость: {}\nЦвет машины: {}\nЦена машины: {}\n".format(
                self.speed, self.top_speed, self.color, self.price
            ))

    def start(self, speed):
        self.speed = speed


car_1 = Toyota(0, 199, "black", 1800000)
car_2 = Toyota(0, 220, "red", 2100000)
car_3 = Toyota(0, 176, "grey", 1400000)
car_1.info()
car_2.start(60)
car_2.info()
car_3.start(100)
car_3.info()
