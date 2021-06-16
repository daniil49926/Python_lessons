def total_price(name):
    rez = 0
    for i_name in range(len(store[goods[name]])):
        rez += store[goods[name]][i_name]["quantity"] * store[goods[name]][i_name]["price"]
    return rez


def total_quantity(name):
    rez = 0
    for i_name in range(len(store[goods[name]])):
        rez += store[goods[name]][i_name]["quantity"]
    return rez


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
for i in ["Лампа", "Стол", "Диван", "Стул"]:
    print("{name} - {num_of_lamp} шт, стоимость {lamp_price} руб".format(
        name=i,
        num_of_lamp=total_quantity(i),
        lamp_price=total_price(i)
    ))

# зачёт! 🚀
