num_of_order = int(input("Введите кол-во заказов: "))
order_dict = dict()
for i in range(num_of_order):
    order = input(f"{i + 1} заказ: ").split()
    if order[0] in order_dict:
        if order[1] in order_dict[order[0]]:
            order_dict[order[0]][order[1]] += int(order[2])
        else:
            order_dict[order[0]][order[1]] = int(order[2])
    else:
        order_dict[order[0]] = {order[1]: int(order[2])}

for i in order_dict:
    print(i)
    for j in sorted(order_dict[i]):
        print("\t", j, ":", order_dict[i][j])

# зачёт! 🚀
