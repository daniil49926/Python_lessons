class Children:
    def __init__(self, name, age, calm=True, hunger=False):
        self.name = name
        self.age = age
        self.calm = calm
        self.hunger = hunger


class Parent:
    def __init__(self, name, age, *args):
        self.name = name
        self.age = age
        self.list_children = list()
        for i in args:
            if self.age - i.age > 0:
                self.list_children.append(i.name)

    def info(self):
        print("Имя - {}\nВозраст - {}\nДети - ".format(
            self.name, self.age
        ), end="")
        for i in self.list_children:
            print(i, end=" ")
        print()

    def calm(self, *args):
        for i in args:
            i.calm = True
            print("{} успокоен".format(i.name))

    def hunger(self, *args):
        for i in args:
            i.hunger = False
            print("{} накормлен".format(i.name))


children1 = Children("Артем", 11, hunger=True, calm=True)
children2 = Children("Коля", 12, hunger=True, calm=False)
children3 = Children("Алена", 70)
par1 = Parent("Олег", 50, children1, children2, children3)
par1.info()
par1.calm(children1, children2)
par1.hunger(children1, children2)

# зачёт! 🚀
