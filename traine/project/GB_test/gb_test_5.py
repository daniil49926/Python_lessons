class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return f'{self.txt}'


inp_data = int(input('Первое число '))  # При вводе данных не приводящихся к типу int ошибка не будет обработанна,
inp_data2 = int(input('Второе число '))  # для правильной работы следует внести ввод в блок try

try:
    inp_data = int(inp_data)  # Данный код можно удалить, т.к. строки при вводе уже будут типа int
    inp_data2 = int(inp_data2)  #

    # Для корректной обработки деления на ноль,
    # следует использовать условный оператор и вызов исключения raise OwnError(текст ошибки)

    z = inp_data / inp_data2

except ZeroDivisionError:   # Обработка деления на 0 будет вызвана при помощи OwnError,
    c = OwnError('Была ошибка')  # поэтому данный блок можно удалить
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:  # else можно удалить и внести вывод ответа в блок кода try
    print(f"Все хорошо. Ваше число: {z}")


"""
Предложенный мною вариант решения задачи 5

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return f'{self.txt}'


try:
    inp_data = int(input('Первое число '))
    inp_data2 = int(input('Второе число '))

    if inp_data2 == 0:
        raise OwnError("Ошибка, деление на 0")

    z = inp_data / inp_data2
    print(f"Все хорошо. Ваше число: {z}")

except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)

"""
