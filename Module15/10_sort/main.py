def sort(num_list):
    new_list = []
    for i in range(len(num_list)):
        minimum = num_list[0]
        for j in range(len(num_list)):
            if minimum > num_list[j]:
                minimum = num_list[j]
        new_list.append(minimum)
        num_list.remove(minimum)
    return new_list


def make_list(num):
    list_num = []
    for i in range(num):
        number = int(input(f"Введите число {i + 1}: "))
        list_num.append(number)
    print(list_num)
    return sort(list_num)


def mod_sort(num):
    num_list = make_list(num)
    for i in range(len(num_list)):
        for j in range(i, len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    print(num_list)


def main():
    number_element = int(input("Введите кол-во элементов: "))
    sort_list = make_list(number_element)
    print(sort_list, "\nМодифицированный вариант:")
    mod_sort(number_element)


main()

# зачёт! 🚀
