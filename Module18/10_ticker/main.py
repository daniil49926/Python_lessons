def reverse_str(first, second):
    count = 0
    if len(first) == len(second):
        for _ in range(len(first)):
            if first == second:
                print("Первая строка получается из второй со сдвигом {num}.".format(
                    num=count
                ))
                return
            else:
                first.append(first[0])
                first.remove(first[0])
                count += 1
        print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
    else:
        print("Строки разной длины!")


first_str = list(input("Введите первую строчку: "))
second_str = list(input("Введите вторую строку: "))
reverse_str(first_str, second_str)

# зачёт! 🚀
