def main():
    try:
        x = float(input("Введите координату x: "))
        y = float(input("Введите координату y: "))
        r = float(input("Введите радиус: "))
        if pow(x, 2) + pow(y, 2) <= pow(r, 2):
            print("Монетка где-то рядом")
        else:
            print("Монетки в радиусе поиска нет")
        main()
    except ValueError:
        print("Ошибка ввода!")
        main()


main()

# зачёт! 🚀
