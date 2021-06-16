goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]

print(goods)
fruit_name = input("Введите название: ")
price = int(input("Введите цену: "))
goods.append([fruit_name, price])
for i in range(len(goods)):
    goods[i][1] *= 1.08
print(goods)