def reverse(num):
    fractional_num = int(100 * round((num - int(num)), 2))
    whole_num = int(num)
    rez1 = cycle(whole_num)
    rez2 = cycle(fractional_num)
    rez2 /= 100
    rez = rez1 + rez2
    return rez


def cycle(num):
    rez = 0
    i = len(str(num)) - 1
    while num > 0:
        rez += (num % 10) * pow(10, i)
        num //= 10
        i -= 1
    return rez


def main():
    N = float(input("Введите первое число: "))
    K = float(input("Введите второе число: "))
    print("\nОбратное первое число:", reverse(N), "\nОбратное второе число:", reverse(K))
    print("\nСумма =", float(reverse(N)) + float(reverse(K)))


main()

# зачёт! 🚀
