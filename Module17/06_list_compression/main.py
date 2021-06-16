num_of_number = int(input("Кол-во чисел: "))
num_list = []
for i in range(num_of_number):
    number = int(input(f"Число {i + 1}: "))
    num_list.append(number)
print(f"Изначальный список: {num_list}")
count = num_list.count(0)
for i in range(count):
    num_list.remove(0)
    num_list.append(0)
print(f"Промежуточный список: {num_list}")
print(f"Итоговый список: {num_list[:len(num_list) - count]}")

# зачёт! 🚀
