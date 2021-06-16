"""
TASK01

num = int(input("Последнее число: "))
square_dict = dict()
for i in range(1, num + 1):
    square_dict[i] = i ** 2
for i in square_dict:
    print(i, ":", square_dict[i])

"""
"""
TASK02

student_info = input("Введите информацию через пробел: ").split()
student_dict = dict()
student_dict["Имя"] = student_info[0]
student_dict["Фамилия"] = student_info[1]
student_dict["Город"] = student_info[2]
student_dict["Место учебы"] = student_info[3]
student_dict["Оценки"] = student_info[4:]

for i in student_dict:
    print(i, ":", student_dict[i])

"""
"""
TASK03

number_dict = dict()
while True:
    try:
        for i in number_dict:
            print(i, ":", number_dict[i])
        name = input("Введите имя: ")
        number = int(input("Введите номер контакта {name}: ".format(
            name=name
        )))
        number_dict[name] = number
    except ValueError:
        print("Ошибка ввода\n")

"""
"""
TASK04

def create_dict(string):
    text_dict = dict()
    for i in string:
        if i in text_dict:
            text_dict[i] += 1
        else:
            text_dict[i] = 1
    draw_diagram(text_dict)


def draw_diagram(text_info):
    for i in text_info:
        print(i, end=" ")
        for j in range(text_info[i]):
            print("#", end="")
        print()
    print("Максимальное кол-во знаков", max(text_info.values()))


text = input("Введите текст").lower()
create_dict(text)

"""
"""
TASK05

small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)
while True:
    answer = input("Введите название товара: ").lower()
    if big_storage.get(answer):
        print(answer, " - ", big_storage.get(answer))
    else:
        print("Такого товара нет на складе")

"""
"""
TASK06

def search_children(member, name_search):
    flag_children = False
    children = member.get("children")
    for i in children:
        name = i.get("name")
        if name == name_search:
            flag_children = True
    if flag_children:
        print("Ребенок найден")
    else:
        print("Ребенок не найден")


family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}
while True:
    name_children = input("Введите имя: ")
    if name_children.casefold() == "end":
        break
    search_children(family_member, name_children)

"""
"""
TASK07

def search_player(team, status):
    team_a = list()
    for i in players_dict:
        if players_dict[i].get("team") == team and players_dict[i].get("status") == status:
            team_a.append(players_dict[i].get("name"))
    print(team_a)


players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}


def main():
    while True:
        team = input("Команда: ")
        status = input("Статус: ")
        if team == "end":
            break
        search_player(team, status)


main()

"""
"""
TASK08

text = input("Введите текст: ")
sign = [".", ",", "!", "?", ":", ";"]
rez = 0
for i in text:
    if i in sign:
        rez += 1
print("Количество знаков пунктуации:", rez)

"""
