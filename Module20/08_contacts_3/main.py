def add_contact(phone_dict):
    name = input("Введите имя нового контакта: ")
    surname = input("Введите фамилию контакта: ")
    phone_number = int(input("Введите номер нового контакта: "))
    for _, value in phone_dict.items():
        if (value["Фамилия"].lower() == surname.lower()) and (value["Имя"].lower() == name.lower()) \
                and (value["Номер"] == phone_number):
            print("Такой контакт уже существует")
            show_book(phone_dict)
            return 0, False
    phone_dict[str(len(phone_dict) + 1)] = {"Фамилия": surname,
                                            "Имя": name,
                                            "Номер": phone_number}
    print("Контакт добавлен\nТекущий список контактов")
    show_book(phone_dict)
    return phone_dict, True


def delete_contact(phone_dict):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone_number = int(input("Введите номер: "))
    for key, value in phone_dict.items():
        if (value["Фамилия"].lower() == surname.lower()) and (value["Имя"].lower() == name.lower()) \
                and (value["Номер"] == phone_number):
            del phone_dict[key]
            print("Контакт удален\nТекущий список контактов")
            show_book(phone_dict)
            return phone_dict, True
    show_book(phone_dict)
    return 0, False


def search_contact(phone_dict):
    surname = input("Введите фамилию: ")
    flag = False
    for key, value in phone_dict.items():
        if value["Фамилия"].lower() == surname.lower():
            flag = True
            print(value)
    if not flag:
        print("Контакт не найден")


def show_book(phone_dict):
    for i_key, i_value in phone_dict.items():
        if i_value.__class__ == dict:
            print("{0}:".format(i_key))
            for j_key, j_value in i_value.items():
                print("\t{0}: {1}".format(j_key, j_value))
        else:
            print("{0}: {1}".format(i_key, i_value))


def main():
    phone_book = {

    }
    while True:
        choice = input("\nДобавить/удалить/найти контакт? ")
        if choice.casefold() == "добавить":
            upd_book, flag = add_contact(phone_book)
            if flag:
                phone_book.update()
        elif choice.casefold() == "удалить":
            if len(phone_book) > 0:
                rem_book, flag_rem = delete_contact(phone_book)
                if flag_rem:
                    phone_book = rem_book
            else:
                print("У вас нет контактов")
        elif choice.casefold() == "найти":
            if len(phone_book) > 0:
                search_contact(phone_book)
            else:
                print("У вас нет контактов")


main()

# зачёт! 🚀
