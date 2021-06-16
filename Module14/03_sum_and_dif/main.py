def summa(number):
    rez = 0
    while number > 0:
        rez += number % 10
        number /= 10
    return int(rez)


def quantity(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


def difference(number):
    return summa(number) - quantity(number)


def main():
    N = int(input("Введите число: "))
    if N > 0:
        count_summa = summa(N)
        count_quantity = quantity(N)
        count_diff = difference(N)
        print("Сумма =", count_summa, "\nКол-во цифр =",
              count_quantity, "\nРазность =", count_diff)
        main()
    else:
        print("Ошибка ввода!")
        main()


main()

# зачёт! 🚀
