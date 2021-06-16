import os

try:
    def writing_file(path, mess):
        save_file = open(path, "w", encoding="UTF-8")
        save_file.write(mess)
        save_file.close()


    text = input("Введите текст: ")
    path_input = input("\nКуда хотите сохранить документ? "
                       "Введите последовательность папок (через пробел):\n").split()
    path_save = os.path.abspath("/")
    for i in path_input:
        path_save = os.path.join(path_save, i)
    name_file = input("Введите название файла: ")
    path_save = os.path.join(path_save, (name_file + ".txt"))
    if os.path.exists(path_save):
        answer = input("Перезаписать файл? да/нет: ")
        if answer.casefold() == "да":
            writing_file(path_save, text)
    else:
        writing_file(path_save, text)

except FileNotFoundError:
    print("Такого пути нет.")

# зачёт! 🚀
