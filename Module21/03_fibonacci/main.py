def fibonacci(num_poz, num1=1, num2=1):
    rez = [num1, num2]
    for i in range(num_poz - 2):
        rez.append(num1 + num2)
        count = num1 + num2
        num1 = num2
        num2 = count
    return rez[num_poz - 1]


position = int(input("Введите место на котором находится число: "))
print(fibonacci(position))

# зачёт! 🚀
