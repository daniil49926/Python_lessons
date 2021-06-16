def print_nums(num):
    if num == 0:
        return  # так тоже можно
    print(num)
    return print_nums(num - 1)


last_num = int(input("Введите последнее число: "))
print_nums(last_num)

# зачёт! 🚀
