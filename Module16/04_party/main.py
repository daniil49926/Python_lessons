def check_guests(name, list_guests):
    return name in list_guests


def add_a_guest(list_guests):
    name = input("Имя гостя: ")
    if len(list_guests) < 6:            # Думаю здесь не нужна проверка на наличие такого же имени
        list_guests.append(name)        # в списке, ведь на этой "тусовке" может быть несколько людей
        print(f"Привет, {name}!\n")     # с одинаковыми именами - да, совершенно верный вывод! ;)
    else:
        print(f"Прости, {name}, но мест нет.\n")
    return list_guests


def delete_a_guest(list_guests):
    name = input("Имя гостя: ")
    if check_guests(name, list_guests):
        list_guests.remove(name)
        print(f"Пока, {name}!\n")
    else:
        print("Такого гостя не было...\n")
    return list_guests


def main(list_guests):
    print(list_guests)
    answer = input("Гость пришел или ушел? ")
    if answer.casefold() == "пришел":
        list_guests = add_a_guest(list_guests)
        main(list_guests)
    elif answer.casefold() == "ушел":
        list_guests = delete_a_guest(list_guests)
        main(list_guests)
    elif answer.casefold() == "пора спать":
        print(f"Спать пошли\n{list_guests}")
    else:
        print("Ошибка ввода!\n")
        main(list_guests)


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
main(guests)

# зачёт! 🚀
