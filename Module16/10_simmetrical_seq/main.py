def sim_seq(num_list):
    reverse_list = []
    for i in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i])
    if num_list == reverse_list:
        return True
    else:
        return False


def main():
    number_list = []
    new_num_list = []
    answer = []
    number_of_num = int(input("Введите кол-во цифр: "))

    for i in range(number_of_num):
        number = int(input(f"Введите {i + 1} число: "))
        number_list.append(number)

    for i in range(len(number_list)):
        for j in range(i, len(number_list)):
            new_num_list.append(number_list[j])
        if sim_seq(new_num_list):
            for k in range(i):
                answer.append(number_list[k])
            answer.reverse()
            break
        new_num_list = []

    print(f"Последовательность: {number_list}\n"
          f"Нужно приписать чисел: {len(answer)}\n"
          f"Сами числа: {answer}")


main()

# зачёт! 🚀
