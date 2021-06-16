import random


class Human:
    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def eat(self):
        eating = random.randint(10, 30)
        if self.house.fridge < eating:
            eating = self.house.fridge
        self.fullness += eating
        self.house.fridge -= eating

    def petting_cat(self):
        self.happiness += 5
        self.fullness -= 10


class Man(Human):
    def work(self):
        self.fullness -= 10
        self.house.box += 150

    def play(self):
        self.fullness -= 10


class Woman(Human):
    def __init__(self, name, house):
        super().__init__(name, house)
        self.fur_coats = 0

    def go_in_shop(self):
        bye_food = random.randint(20, 22)
        bye_cat_food = random.randint(4, 5)
        if self.house.box < bye_food + bye_cat_food:
            bye_food = self.house.box / 2
            bye_cat_food = self.house.box / 2
        else:
            if self.house.fridge > 100:
                bye_food = 0
            if self.house.fridge > 50:
                bye_cat_food = 0
        self.house.fridge += bye_food
        self.house.box -= bye_food + bye_cat_food
        self.house.cat_food += bye_cat_food

    def bye_fur_coat(self):
        self.fur_coats += 1
        self.house.box -= 350

    def clearing_house(self):
        clearing = random.randint(50, 100)
        if self.house.dirty < clearing:
            clearing = self.house.dirty
        self.fullness -= 10
        self.house.dirty -= clearing


class Cat:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30

    def eat(self):
        eating = random.randint(5, 10)
        if cat.house.cat_food < eating:
            eating = cat.house.cat_food
        self.fullness += eating * 2
        self.house.cat_food -= eating

    def sleep(self):
        self.fullness -= 10

    def spoil_wallpaper(self):
        self.house.dirty += 5


class House:
    def __init__(self):
        self.fridge = 50
        self.box = 100
        self.cat_food = 30
        self.dirty = 0


def man_life(human):
    if human.house.dirty > 90:
        human.happiness -= 10
    if human.fullness < 40:
        human.eat()
    elif human.happiness < 50:
        human.petting_cat()
    elif human.house.box < 100:
        human.work()
    else:
        human.play()


def woman_life(human):
    if human.house.dirty > 90:
        human.happiness -= 10
    if human.house.dirty > 80:
        human.clearing_house()
    elif human.fullness < 40:
        human.eat()
    elif human.happiness < 50:
        human.petting_cat()
    elif human.house.fridge < 30 or human.house.cat_food < 10:
        human.go_in_shop()
    elif human.house.box > 500:
        human.bye_fur_coat()


def cat_life(animal):
    if animal.fullness < 15:
        animal.eat()
    else:
        choice = random.randint(1, 2)
        if choice == 1:
            animal.sleep()
        if choice == 2:
            animal.spoil_wallpaper()


house = House()
man = Man("Антон", house)
woman = Woman("Алиса", house)
cat = Cat("Рыжик", house)
for i in range(365):
    if man.fullness < 0 or man.happiness < 10:  # Рандом конечно делает свое и не всегда все выживают
        print("{} умер".format(
            man.name
        ))
        break
    if woman.fullness < 0 or woman.happiness < 10:
        print("{} умерла".format(
            woman.name
        ))
        break
    if cat.fullness < 0:
        print("{} умер".format(
            cat.name
        ))
        break
    house.dirty += 5
    man_life(man)
    woman_life(woman)
    cat_life(cat)
print(f"Муж:\n"
      f"\tСытость - {man.fullness}\n"
      f"\tСчастье - {man.happiness}\n"
      f"Жена:\n"
      f"\tСытость - {woman.fullness}\n"
      f"\tСчастье - {woman.happiness}\n"
      f"\tКол-во шуб - {woman.fur_coats}\n"
      f"Кот:\n"
      f"\tСытость - {cat.fullness}\n"
      f"Дом:\n"
      f"\tКол-во денег - {house.box}\n"
      f"\tКол-во еды в холодильнике - {house.fridge}\n"
      f"\tКол-во еды у кота - {house.cat_food}\n"
      f"\tКол-во грязи - {house.dirty}")

# зачёт! 🚀
# отлично получилось!
