def lcd(num):
    for i in range(2, num + 1):
        if num % i == 0:
            return i


def main():
    number = int(input("Введите число: "))
    divider = lcd(number)
    print("Наименьший общий делитель: ", divider, "\n\n")
    main()


main()

# зачёт! 🚀
