import random


class Student:
    def __init__(self, name, num_group, score):
        self.name = name
        self.num_group = num_group
        self.score = score


def take_elem(inp_list):
    return inp_list[2]


my_list = list()
for i_name in "Даниил Армен Егор Никита Артем Антон Сергей Вадим Дмитрий Владислав".split():
    student = Student(i_name, random.randint(1, 5), random.randint(0, 100))
    my_list.append([student.name, student.num_group, student.score])
my_list.sort(key=take_elem)
for i_elem in my_list:
    print(i_elem[0], i_elem[1], i_elem[2])

# зачёт! 🚀
