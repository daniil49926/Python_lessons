class Person:
    __count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = self.set_age(age)
        Person.__count += 1

    def get_count(self):
        return self.__count

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age in range(1, 90):
            self.__age = age
            return age
        else:
            raise Exception("Такой возраст не доступен")


misha = Person("Миша", 19)
anton = Person("Антон", 30)
print(misha.get_age())
misha.set_age(20)
print(misha.get_age())
print(misha.get_count())