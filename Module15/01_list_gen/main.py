def odd_integer(num):
    list_odd_integer = []
    for i in range(1, num + 1, 2):
        list_odd_integer.append(i)
    return list_odd_integer


def main():
    last_num = int(input("Введите последнее число списка: "))
    print(f"Список нечетных чисел от 1 до {last_num}:\n", odd_integer(last_num))
    main()


main()

# зачёт! 🚀
