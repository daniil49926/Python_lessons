"""
TASK01

try:
    BRUCE_WILLIS = 42

    input_data = input('Введите строку: ')
    leeloo = int(input_data[4])

    result = BRUCE_WILLIS * leeloo

    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError:
    print("Невозможно умножить на 5 элемент")
except IndexError:
    print("выход за границы списка")

"""
"""
TASK02

file = open("lesson15.txt", "w")
try:
    nums = int(input("Ввод: "))
    file.write(str(nums))
except ValueError:
    print("Ошибка ввода")
finally:
    file.close()
    print("Файл закрыт")
    
"""