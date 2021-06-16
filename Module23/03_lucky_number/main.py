import random


def my_random():
    return random.randint(0, 13)


def rand_exception():
    return random.choice(Exception.__subclasses__())


rez = 0
while rez < 777:
    if my_random():
        try:
            inp_num = int(input("Введите число: "))
        except ValueError:
            print("Это не число!")
        else:
            rez += inp_num
    else:
        raise rand_exception()
print("Поздравляем, вы выиграли в этой рулетке!)")

# зачёт! 🚀
