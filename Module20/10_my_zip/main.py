def my_zip(a, b):
    for i in range(min((len(a), len(b)))):
        print((a[i], b[i]))


text = input("Введите строку: ")
list_tuple = input("Введите кортеж, без скобок: ").split(", ")
num_tuple = tuple(list_tuple)
print(my_zip)
my_zip(text, num_tuple)

# зачёт! 🚀
