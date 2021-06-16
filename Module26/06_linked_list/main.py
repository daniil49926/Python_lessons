class LinkedList:
    def __init__(self) -> None:
        self.values = ""

    def append(self, num) -> None:
        self.values += f" {num} "

    def __str__(self) -> str:
        return "[" + str(self.values) + "]"

    def get(self, num: int) -> int:
        a = self.values.split("  ")
        return int(a[num])

    def remove(self, num: int) -> None:
        count = ""
        a = self.values.split("  ")
        for i in a:
            if i != a[num]:
                count += i + " "
        self.values = count[0:-1]


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

# зачёт! 🚀
