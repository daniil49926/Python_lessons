"""
TASK01
"""


class Pet:
    def __init__(self):
        self.legs = 4
        self.tail = 1


class Cat(Pet):
    def __init__(self):
        super().__init__()
        self.__song = "Мяу"

    def get_legs(self):
        return self.legs

    def get_tails(self):
        return self.tail

    def __str__(self):
        return self.__song


class Dog(Pet):
    def __init__(self):
        super().__init__()
        self.__song = "Гав"

    def get_legs(self):
        return self.legs

    def get_tails(self):
        return self.tail

    def __str__(self):
        return self.__song


dog = Dog()
cat = Cat()
print(cat)
print(cat.get_legs())


"""
TASK02
"""


class Ship:
    def __init__(self, model):
        self.model = model

    def sails(self):
        print("Корабль {} плывет".format(
            self.model
        ))


class WarShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model=model)
        self.__gun = gun

    def fire(self):
        print("{} произвел выстрел из {}".format(
            self.model, self.__gun
        ))


class CargoShip(Ship):
    def __init__(self, model, cargo):
        super().__init__(model=model)
        self.__cargo = cargo

    def unload(self):
        self.__cargo -= 1
        print("Кол-во грузов на корабле - {}".format(
            self.__cargo
        ))

    def load(self):
        self.__cargo += 1
        print("Кол-во грузов на корабле - {}".format(
            self.__cargo
        ))


war_ship = WarShip("w3q", "мортира")
war_ship.fire()
war_ship.sails()
cargo_ship = CargoShip("Морская лавина", 10)
cargo_ship.sails()
cargo_ship.unload()
cargo_ship.load()












