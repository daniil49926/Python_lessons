import os

"""
TASK01

def print_dir(project):
    print("\nСодержимое директории", project)
    for i_elem in os.listdir(project):
        print(os.path.abspath(i_elem))


project_list = ["ProjectPySkiilbox", "python_basic"]
for i_proj in project_list:
    path_to_project = os.path.abspath(os.path.join("..", "..", i_proj))
    print_dir(path_to_project)

print("\n\n", os.listdir("C:/Program Files (x86)/Notepad++"))

"""

"""
TASK02

path = os.path.join("Skillbox", "access", "admin.bat")
abs_path = os.path.abspath(path)
print(path + "\n" + abs_path)

"""
"""
TASK03

for i in os.listdir(os.path.abspath(os.path.join("/", "python_basic"))):
    print(os.path.abspath(i))
"""
"""
TASK04
path = (os.path.abspath(""))
print(path[:3])
"""
"""
TASK05

input_path = input("Введите путь: ")
if os.path.isdir(input_path):
    print("Это папка")
elif os.path.isfile(input_path):
    print("Это файл")
    print(os.path.getsize(input_path), "байт")
elif os.path.islink(input_path):
    print("Это ссылка")
else:
    print("Такого пути не существует")
"""

"""
TASK06

def opened_file(name_file):
    input_file = open("Work_with_file/Additional_info/{name_file}".format(
        name_file=name_file
    ), "r", encoding="UTF-8")
    for i_line in input_file:
        print(i_line, end="")
    input_file.close()
    print("\n")


opened_file("group_1.txt")
opened_file("group_2.txt")
"""
"""
TASK07

def search_file(cur_path, name_file):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if name_file == i_elem:
            return path
        if os.path.isdir(path):
            rez = search_file(path, name_file)
            if rez:
                break
    else:
        rez = None
    return rez


input_name = input("Введите имя файла: ")
file_path = search_file(os.path.join("..", "ProjectPySkiilbox"), input_name)
readable_file = open(file_path, "r", encoding="UTF-8")
for i in readable_file:
    print(i, end="")
readable_file.close()
history_search = open(os.path.join("D:/ProjectPySkiilbox/Work_with_file/Additional_info/history"), "a", encoding="UTF-8")
history_search.write(file_path + "\n")
history_search.close()
"""
"""
TASK08

num_file = open("D:/ProjectPySkiilbox/Work_with_file/Additional_info/num.txt", "r", encoding="UTF-8")
rez = 0
for i in num_file:
    rez += int(i)
num_file.close()
rez_file = open("D:/ProjectPySkiilbox/Work_with_file/Additional_info/rez.txt", "a", encoding="UTF-8")
rez_file.write(str(rez))
rez_file.close()
"""


