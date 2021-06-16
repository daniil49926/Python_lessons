class Water:
    def __init__(self):
        self.name = "Вода"

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Fire):
            return Vapor()
        if isinstance(other, Earth):
            return Dirt()


class Air:
    def __init__(self):
        self.name = "Воздух"

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()
        if isinstance(other, Water):
            return Storm()


class Fire:
    def __init__(self):
        self.name = "Огонь"

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        if isinstance(other, Air):
            return Lightning()
        if isinstance(other, Water):
            return Vapor()


class Earth:
    def __init__(self):
        self.name = "Земля"

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Water):
            return Dirt()


class Storm:
    def __init__(self):
        self.name = "Шторм"


class Vapor:
    def __init__(self):
        self.name = "Пар"


class Dirt:
    def __init__(self):
        self.name = "Грязь"


class Lightning:
    def __init__(self):
        self.name = "Молния"


class Dust:
    def __init__(self):
        self.name = "Пыль"


class Lava:
    def __init__(self):
        self.name = "Лава"

    def __str__(self):  # так тоже можно
        return self.name


a = Fire()
b = Earth()
c = b + a
print(c)

# зачёт! 🚀
