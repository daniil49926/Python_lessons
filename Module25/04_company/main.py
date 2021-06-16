import random


class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):

    def salary(self):
        return "{} {} зарабатывает".format(
            self.get_name(), self.get_surname()
        )


class Manager(Employee):
    __sal = 13000

    def salary(self):
        info = super().salary()
        info = " - ".join(
            (
                info,
                str(self.__sal)
            )
        )
        return info


class Agent(Employee):
    __sal = 5000
    __percent = int() * 0.05

    def __init__(self, name, surname, age):
        super().__init__(name=name, surname=surname, age=age)
        self.__percent = random.randint(1000, 20000) * 0.05  # Внес в инициализацию для получения рандома для каждого

    def salary(self):
        info = super().salary()
        info = " - ".join(
            (
                info,
                str(self.__sal + self.__percent)
            )
        )
        return info


class Worker(Employee):
    __nums_day = int()

    def __init__(self, name, surname, age):
        super().__init__(name=name, surname=surname, age=age)
        self.__nums_day = random.randint(1, 30)  # Внес в инициализацию для получения рандома для каждого

    def salary(self):
        info = super().salary()
        info = " - ".join(
            (
                info,
                str(100 * self.__nums_day)
            )
        )
        return info


salary_list = [
    Manager(name="Артем", surname="Артемов", age=22),
    Manager(name="Антон", surname="Антонов", age=40),
    Manager(name="Армен", surname="Арменов", age=25),
    Agent(name="Олег", surname="Олегов", age=21),
    Agent(name="Андрей", surname="Андреев", age=24),
    Agent(name="Даниил", surname="Даниилов", age=18),
    Worker(name="Ирина", surname="Иринова", age=18),
    Worker(name="Алиса", surname="Алисова", age=18),
    Worker(name="Наталья", surname="Натальевв", age=18),
]
for i in salary_list:
    print(i.salary())

# зачёт! 🚀
