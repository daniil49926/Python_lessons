number_friend = int(input("Кол-во друзей: "))
number_debt = int(input("Кол-во расписок: "))
friend_list = []
for i in range(number_friend):
    friend_list.append([i, 0])
for i in range(number_debt):
    print(f"Расписка №{i + 1}")
    to_ = int(input(f"Кому: "))
    from_ = int(input(f"От кого: "))
    how_much = int(input(f"Сколько: "))
    friend_list[to_ - 1][1] += how_much
    friend_list[from_ - 1][1] -= how_much
for i in range(number_friend):
    print(f"{friend_list[i][0] + 1} : {friend_list[i][1]}")

# зачёт! 🚀
