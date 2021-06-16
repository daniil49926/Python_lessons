def search(first_list, second_list):
    rez = 0
    for i in range(len(second_list)):
        for j in range(len(first_list)):
            if second_list[i] <= first_list[j]:
                rez += 1
                first_list.remove(first_list[j])
                break
    return rez


def main():
    rollers_list = []
    people_list = []
    number_rollers = int(input(f"Кол-во роликов: "))
    for i in range(number_rollers):
        size_roller = int(input(f"Введите размер {i + 1} роликов: "))
        rollers_list.append(size_roller)
    number_people = int(input(f"Кол-во людей: "))
    for i in range(number_people):
        size_legs = int(input(f"Введите размер ноги {i + 1} человека: "))
        people_list.append(size_legs)
    rollers_list.sort()
    people_list.sort()
    print(f"Наибольшее кол-во людей, которые могут взять ролики: "
          f"{search(rollers_list, people_list)}")


main()

# зачёт! 🚀
