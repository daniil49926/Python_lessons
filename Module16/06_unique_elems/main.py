first_list = []
second_list = []
for i in range(3):
    number = int(input(f"Введите {i + 1} число из первого списка: "))
    first_list.append(number)
for i in range(7):
    number = int(input(f"Введите {i + 1} число из второго списка: "))
    second_list.append(number)

print(f"Первый список: {first_list}\nВторой список{second_list}")
first_list.extend(second_list)
finish_list = []                                # Добавил еще один список для более корректного вывода
finish_list.extend(set(first_list))
print(f"Итоговый список: {finish_list}")

# зачёт! 🚀
