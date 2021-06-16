def search(list_cells):
    rez = ''
    for rang in range(len(list_cells)):
        if rang > list_cells[rang]:
            rez += str(list_cells[rang])
            rez += " "
    return rez


def cycle(num):
    list_cells = []
    for i in range(num):
        cell_efficiency = int(input(f"Эффективность {i + 1} клетки: "))
        list_cells.append(cell_efficiency)
    rez = search(list_cells)
    return rez


def main():
    numbers_cells = int(input("Введите кол-во клеток: "))
    rez = cycle(numbers_cells)
    print("Неподходящие значения", rez)


main()

# зачёт! 🚀
