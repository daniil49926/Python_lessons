"""
TASK01

def factorial(num_fact):
    if num_fact > 900:
        return "Число слишком большое"
    if num_fact == 1:
        return 1
    interim_fact = factorial(num_fact - 1)
    return num_fact * interim_fact


num = int(input("Введите число: "))
print(factorial(num))

"""
"""
TASK02

def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


float_num = float(input('Введите вещественное число: '))
int_num = int(input('Введите степень числа: '))
print(float_num, '**', int_num, '=', power(float_num, int_num))

"""

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
"""
TASK03

def search(search_key, struct):
    if search_key in struct:
        return struct[search_key]
    for i in struct.values():
        if isinstance(i, dict):
            result = search(search_key, i)
            if result:
                break
    else:
        result = None
    return result


key = input("Введите ключ: ")
rez = search(key, site)
if rez:
    print(rez)
else:
    print("Такого ключа нет.")

"""
"""
TASK04

import random
import copy


def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)


nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
dict1 = copy.deepcopy(common_dict)
change_dict(dict1)
print(dict1)
print(common_dict)

"""

"""
TASK05

def ask_answer(question,
               answer="Введите 'да' или 'нет'",
               num_of_attempt=4):
    input_answer = input(question)
    if input_answer == "да":
        return 1
    if input_answer == "нет":
        num_of_attempt -= 1
        print("Осталось попыток", num_of_attempt)
        ask_answer(question, answer, num_of_attempt)
    else:
        print(answer)
        num_of_attempt -= 1
        print("Осталось попыток", num_of_attempt)
        ask_answer(question, answer, num_of_attempt)


ask_answer("Выйти: ",
           num_of_attempt=2)
ask_answer("Сохранить: ",
           answer="Так сохранить или нет",
           num_of_attempt=5)
ask_answer("Создать? ",
           num_of_attempt=1)
           
"""
"""
TASK06

def func(num, list_num=None):
    if list_num is None:
        list_num = list()
    while num != 0:
        list_num.append(num)
        num -= 1
    print(list_num)


func(5)
func(10, list_num=[0, 0, 0, 0, 9])
func(15)

"""
"""
TASK07

def create_dict(data_, template=None):
    if template is None:
        template = dict()
    if isinstance(data_, dict):
        return data_
    elif isinstance(data_, int) or isinstance(data_, float) or isinstance(data_, str):
        template[data_] = data_
        return template


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        rez = create_dict(i_element)
        if rez:
            new_list.append(create_dict(i_element))
    return new_list


data = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data)
print(data)

"""
"""
TASK08

def my_func(name, storage1=None, storage2=None):
    if storage1 is not None:
        storage1 = storage1 * 1.11
    if storage2 is not None:
        storage2 = storage2 * 2.22
    print("Имя", name)
    print("Storage1", storage1)
    print("Storage2", storage2)


my_func("Магазин", 200)
my_func("Еще магаз", storage2=400)
my_func("Привет")

"""