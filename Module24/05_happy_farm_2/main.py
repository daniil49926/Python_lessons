class Potato:
    states = {0: "Отсутствует", 1: "Росток", 2: "Зеленая", 3: "Зрелая"}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print("Картошка {} сейчас {}".format(
            self.index, Potato.states[self.state]
        ))


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print("\nКартошка прорастает")
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potatoes:
            if not i_potato.is_ripe():
                print("\nКартошка еще не созрела")
                break
        else:
            print("\nВся картошка созрела. Можно собирать")


class Gardener:
    def __init__(self, name, name_garden):
        self.name = name
        self.garden = name_garden.potatoes
        self.count_potatoes = 0

    def grow_potatoes(self):
        if self.garden is not None:
            print("\nКартошка прорастает, после работы садовника...")
            for i_potato in self.garden:
                i_potato.grow()
        else:
            print("\nЭта грядка пуста")

    def collect_potatoes(self):
        for i_potato in self.garden:
            if not i_potato.is_ripe():
                break
        else:
            self.garden = None
            print("\nСадовник собрал картофель\n")


my_garden = PotatoGarden(5)
my_garden.grow_all()
my_garden.are_all_ripe()
my_gardener = Gardener("Василий", my_garden)
my_gardener.grow_potatoes()
my_gardener.grow_potatoes()

my_gardener.collect_potatoes()
my_gardener.grow_potatoes()
my_garden = PotatoGarden(2)
my_garden.grow_all()

# зачёт! 🚀
