max_number = int(input("Введите макс число: "))
possible_numbers = set(i for i in range(1, max_number + 1))
new_num = []
while True:
    numbers = input("Нужное число есть среди вот этих чисел: ").split()
    if numbers[0] == "Помогите!":
        print("Артём мог загадать следующие числа: {num}".format(
            num=possible_numbers
        ))
        break
    numbers = numbers
    for i in numbers:
        new_num.append(int(i))

    answer = input("Ответ Артёма: ")
    if answer.casefold() == "да":
        possible_numbers = possible_numbers & set(new_num)
        new_num.clear()
    elif answer.casefold() == "нет":
        possible_numbers = possible_numbers - set(new_num)
        new_num.clear()

# зачёт! 🚀
