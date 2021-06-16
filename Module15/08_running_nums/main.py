number_items = int(input("Сколько элементов всего: "))
list_items = []
step = int(input("Введите шаг: "))

for i in range(number_items):
    item = int(input(f"Введите элемент {i + 1}: "))
    list_items.append(item)
print(list_items)

for i in range(step):
    list_items.insert(0, len(list_items) - i)
    list_items.pop(len(list_items) - 1)
print(list_items)

# зачёт! 🚀
