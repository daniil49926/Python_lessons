data_base = {
    ("Сидоров", "Никита", 35),
    ("Петров", "Никита", 15),
    ("Андреева", "Александар", 25),
    ("Сидорова", "Алина", 20),
    ("Антонов", "Антон", 9),
    ("Алексеев", "Артем", 19),
    ("Сидоров", "Павел", 28),
    ("Антонов", "Не Антон", 95),
    ("Петров", "Олег", 35),
    ("Андреев", "Никита", 31),
}

surname = input("Введите фамилию: ")
for i in data_base:
    if i[0].lower() == surname.lower():
        print(i)
    elif i[0].lower() == surname.lower() + "а":
        print(i)
    elif i[0].lower() + "а" == surname.lower():
        print(i)

# зачёт! 🚀
