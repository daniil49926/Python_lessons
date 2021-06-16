def search(list_num):
    maximum = list_num[0]
    for i in range(len(list_num)):
        if maximum < list_num[i]:
            maximum = list_num[i]
    new_list = []
    for i in range(len(list_num)):
        if list_num[i] != maximum:
            new_list.append(list_num[i])
    return new_list


def make_list(num):
    list_num = []
    for i in range(num):
        ver = int(input(f"{i + 1} видеокарта: "))
        list_num.append(ver)
    print("Старый список видеокарт:\n", list_num)
    return search(list_num)


def main():
    videocards = int(input("Введите кол-во видеокарт: "))
    print("Новый список видеокарт:\n", make_list(videocards))


main()

# зачёт! 🚀
