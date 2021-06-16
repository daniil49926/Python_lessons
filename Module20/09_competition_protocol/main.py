num_of_records = int(input("Сколько записей вводится в протокол: "))
print("Записи (результат и имя): ")
score_list = []
for i in range(num_of_records):
    recording = input(f"{i + 1} запись: ").split()
    score_list.append([int(recording[0]), recording[1]])

score_list.sort(key=lambda k: k)
rez_list = []
for i in score_list[::-1]:
    if i[1] not in rez_list:
        rez_list.append(i[0])
        rez_list.append(i[1])

rez_list = rez_list[::-1]
print("Итоги соревнований:")
for i in range(3):
    maximum = rez_list[1]
    name_max = rez_list[0]
    for j in range(1, len(rez_list), 2):
        if rez_list[j] > maximum:
            maximum = rez_list[j]
            name_max = rez_list[j - 1]
    print(f"{i + 1} место. {name_max} ({maximum})")
    rez_list.remove(maximum)
    rez_list.remove(name_max)

# зачёт! 🚀
