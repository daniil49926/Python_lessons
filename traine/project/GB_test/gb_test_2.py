class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Активный предмет {obj}".format(
            obj=self.title
        )


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Активный предмет {obj}".format(
            obj=self.title
        )


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return "Активный предмет {obj}".format(
            obj=self.title
        )


pen = Pen(title="ручка")
pencil = Pencil(title="карандаш")
handle = Handle(title="маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())

