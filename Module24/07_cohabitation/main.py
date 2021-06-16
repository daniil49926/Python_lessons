import random


class Human:
    def __init__(self, name, house):
        self.name = name
        self.fullness = 50
        self.house = house

    def eat(self):
        self.fullness += 10
        self.house.fridge -= 10

    def work(self):
        self.fullness -= 10
        self.house.box += 10

    def play(self):
        self.fullness -= 10

    def go_in_shop(self):
        self.house.fridge += 10
        self.house.box -= 10

    def info(self):
        print("{}\nСытость - {} Еды дома - {} Денег дома {}".format(
            self.name, self.fullness, self.house.fridge, self.house.box
        ))


class House:
    def __init__(self):
        self.fridge = 50
        self.box = 0


def life(human):
    num = random.randint(1, 6)
    if human.fullness < 20:
        human.eat()
    elif human.house.fridge < 10:
        human.go_in_shop()
    elif human.house.box < 50:
        human.work()
    elif num == 1:
        human.work()
    elif num == 2:
        human.eat()
    else:
        human.play()


house = House()
human1 = Human("Антон", house)
human2 = Human("Олег", house)
for i in range(365):
    if human1.fullness < 0:
        print("{} умер".format(
            human1.name
        ))
        break
    if human2.fullness < 0:
        print("{} умер".format(
            human2.name
        ))
        break
    life(human1)
    life(human2)
print("Все норм, люди выжили")
human1.info()
human2.info()

# зачёт! 🚀
