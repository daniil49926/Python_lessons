import random


class Card:
    def __init__(self, num, color):
        self.num_card = num
        self.color_card = color

    def info(self):
        print(self.num_card, self.color_card)


def add_to_hand(inp_list, nums_card):
    for _ in range(nums_card):
        card = random.choice(card_list)
        inp_list.append(card)
        card_list.remove(card)


def search_11(inp_list):
    flag = False
    for card in inp_list:
        if card.num_card == 11:
            card.num_card -= 10
            flag = True
    return flag


card_list = []
for num_card in [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]:
    for class_card in ["card_of_heart", "card_of_diamond", "card_of_club", "card_of_spade"]:
        card_list.append(Card(num_card, class_card))

user_list = []
computer_list = []
add_to_hand(user_list, 2)
add_to_hand(computer_list, 2)
count_user = 0
count_computer = 0
while True:
    count_user = 0
    for i in user_list:
        count_user += i.num_card
        i.info()
    if count_user > 21:
        if search_11(user_list):
            print("Карты в пересчете: ")
            continue
        count_user -= 21
        print("Вы сгораете")
        break
    choice = input("Взять карту/Остановиться? (1/0) ")
    if choice == "1":
        add_to_hand(user_list, 1)
    else:
        break

while True:
    count_computer = 0
    for i in computer_list:
        count_computer += i.num_card
    if count_computer > 21:
        if search_11(computer_list):
            continue
        count_computer -= 21
        break
    if count_computer < 17:
        add_to_hand(computer_list, 1)
    else:
        break

print("Ваши очки - {}\nОчки компьютера - {}".format(
    count_user, count_computer
))
if count_user > count_computer:
    print("Вы победили")
elif count_user == count_computer:
    print("Ничья")
else:
    print("Вы проиграли")

# зачёт! 🚀
