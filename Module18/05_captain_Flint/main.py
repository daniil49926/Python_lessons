OY = input("По оси OY: ").split()
OX = input("По оси OX: ").split()
x, y = 0, 0
if OY[0].casefold() == "south":
    y = -1
elif OY[0].casefold() == "north":
    y = 1
else:
    print("Ошибка: такого направления OY нет.")
if OX[0].casefold() == "east":
    x = 1
elif OX[0].casefold() == "west":
    x = -1
else:
    print("Ошибка: такого направления OX нет.")
print("Результат:", int(OX[1]) * x, int(OY[1]) * y)

# зачёт! 🚀
