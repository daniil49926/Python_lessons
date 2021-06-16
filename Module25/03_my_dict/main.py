class MyDict(dict):
    def __init__(self):
        super().__init__()

    def get(self, key, default=0, /):
        if key in self:
            return self.__getitem__(key)
        else:
            return 0


my_dict = MyDict()
my_dict["a"] = 1
my_dict["b"] = 2
print("Модифицированный dict")
print(my_dict.get("a"))
print(my_dict.get("g"))
print(my_dict)

my_dict2 = dict()
my_dict2["a"] = 1
my_dict2["b"] = 2
print("Обычный dict")
print(my_dict2.get("a"))
print(my_dict2.get("g"))
print(my_dict2)

# зачёт! 🚀
