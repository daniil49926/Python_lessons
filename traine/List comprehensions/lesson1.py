"""
TASK01

start = int(input("Левая граница: "))
stop = int(input("Правая граница: "))
print(f"{[i ** 3 for i in range(start, stop + 1)]}\n{[i ** 2 for i in range(start, stop + 1)]}")

"""
"""
TASK02

message = input("Введите сообщение: ")
sign = input("Введите символ: ")
print(f"Сообщение с удвоенными знаками: {[i * 2 for i in message]}\n"
      f"Сообщение с доп.знаком{[(i * 2) + sign for i in message]}")
      
"""
"""
TASK03

def new_price(num, percent):
    return round(num * (1 + (percent / 100)), 2)


number_prices = int(input("Кол-во цен: "))
list_price = []
for i in range(number_prices):
    price = float(input(f"Введите {i + 1} цену: "))
    list_price.append(price)
first_percent = float(input("Первый процент: "))
second_percent = float(input("Второй процент: "))
new_list_price = [new_price(i, first_percent) for i in list_price]
print(f"{new_list_price}\n"
      f"{[new_price(i, second_percent) for i in new_list_price]}")

"""
"""
TASK04 

import random

squad_1 = [random.randint(50, 80) for _ in range(10)]
squad_2 = [random.randint(30, 60) for _ in range(10)]
squad_3 = [("Выжил" if squad_1[i] + squad_2[i] > 100 else "Погиб") for i in range(10)]
survived = squad_3.count("Выжил")
died = squad_3.count("Погиб")
print(f"{squad_3}\nВыжило: {survived}\nПогибло: {died}")

"""

"""
TASK05

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_prices = [i for i in original_prices if i > 0]
print(new_prices)

"""














