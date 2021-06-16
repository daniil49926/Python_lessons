"""
TASK01

import random


def rand_tuple(a, b):
    num_list = []
    for i in range(10):
        num_list.append(random.randint(a, b))
    return tuple(num_list)


first_tuple = rand_tuple(0, 5)
second_tuple = rand_tuple(-5, 0)
third_tuple = first_tuple + second_tuple
print(third_tuple, "\n",
      "Кол-во '0'", third_tuple.count(0))

"""
"""
TASK02

def cipher(text):
    first_cipher = "а че ты тут ждал?"
    second_cipher = list(text)
    second_cipher.reverse()
    new_second_cipher = ""
    for i in second_cipher:
        new_second_cipher += i 
    return first_cipher, new_second_cipher


def main():
    text = input("Введите текст: ")
    print("Первый вариант шифра {first_cipher}\nВторой вариант шифра {second_cipher}".format(
        first_cipher=cipher(text)[0],
        second_cipher=cipher(text)[1]
    ))


main()

"""
"""
TASK03

text = input("Введите текст: ")
for i_text, i_sign in enumerate(text):
    if i_sign == "~":
        print(i_text)

"""
"""
TASK04

def dict_creator(sign_list):
    cr_dict = {}
    for i_list, i_sign in enumerate(sign_list):
        cr_dict[i_list] = i_sign
    print(cr_dict)


first_list = ["a", "b", "c", "e"]
second_list = ["g", "h", "o"]
dict_creator(first_list)
dict_creator(second_list)

"""
"""
TASK05

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

for name, cost in incomes.items():
    print(name, "--", cost)

"""
"""
TASK06

server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i_key, i_value in server_data.items():
    if i_value.__class__ == dict:
        print("{0}:".format(i_key))
        for j_key, j_value in i_value.items():
            print("\t{0}: {1}".format(j_key, j_value))
    else:
        print("{0}: {1}".format(i_key, i_value))
"""
"""
TASK07 

data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}
series = int(input("Серия: "))
number = int(input("Номер: "))
for key, value in data.items():
    if series in key and number in key:
        print(value[0], value[1])

"""