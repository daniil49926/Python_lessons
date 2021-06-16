import datetime


def view_chat():
    with open("chat.txt", "r", encoding="UTF-8") as file:
        for i_line in file:
            print(i_line)


def write_mess(name):
    with open("chat.txt", "a", encoding="UTF-8") as file:
        mess = input()
        now = datetime.datetime.now()
        file.write(f"{name} ({now.hour}:{now.minute} {now.day}.{now.month}.{now.year}): {mess}\n")


inp_name = input("Введите имя: ")
while True:
    choice = input("что хотите сделать?\n"
                   "1 - Просмотреть чат\n"
                   "2 - Написать сообщение\n"
                   "3 - Завершить программу\n")
    if choice == "1" or choice.casefold() == "просмотреть чат":
        view_chat()
    if choice == "2" or choice.casefold() == "написать сообщение":
        write_mess(inp_name)
    if choice == "3" or choice.casefold() == "завершить программу":
        break

# зачёт! 🚀
