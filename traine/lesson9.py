"""
task01

template = "Здравствуйте, {name}! Ваш номер заказа: {number}. Приятного дня!"
name = input("Введите имя: ")
number = input("Номер заказа: ")
print(template.format(
    name=name,
    number=number
))
"""
"""
task02

template = "{name}! {name}, привет! Как дела, {name}? Где мои {debt}? {name}!"
name = input("Введите ваше имя: ")
debt = input("Сколько должны: ")
print(template.format(
    name=name,
    debt=debt
))

"""
"""
task03

text = input("Введите текст: ").split()
new_text = " ".join(text)
print("Исправленный текст {text}".format(
    text=new_text
))

"""
"""
task04

def main():
    template = input("Введите шаблон ({name}/{age}): ")
    if "{name}" and "{age}" in template:
        while True:
            name = input("Введите имена через ',': ").split(",")
            ages = input("Введите возраст через пробел: ").split()
            for i in range(len(name)):
                print(template.format(
                    name=name[i],
                    age=ages[i]
                ))
            people = [" ".join([name[i], str(ages[i])]) for i in range(len(name))]
            print("Именинники: ", " ".join(people))
    else:
        print("Вы не ввели конструкции в шаблоне")
        main()


main()

"""
"""
task05

way = input("Введите путь: ")
if not way.startswith("C:/"):
    print("Неправильный диск!")
elif not way.endswith("txt"):
    print("Неправильное расширение файла!")
else:
    print("Путь правильный\n{way}".format(
        way=way
    ))

"""
"""
task06

text = input("Введите текст: ")
low = 0
upp = 0
for i in text:
    if i.islower():
        low += 1
    elif i.isupper():
        upp += 1
print(text.lower() if low > upp else text.upper())

"""