number_containers = int(input("Введите кол-во контейнеров: "))
list_containers = []
try:
    for i in range(number_containers):
        weight_container = int(input(f"Введите вес {i + 1} контейнера: "))
        list_containers.append(weight_container)

    new_container = int(input("Введите вес нового контейнера: "))
    for i in range(number_containers + 1):
        if list_containers[i] < new_container:
            print(f"Номер, куда встанет новый контейнер: {i + 1}")
            break

except IndexError:
    print(f"Номер, куда встанет новый контейнер: {number_containers + 1}")

# зачёт! 🚀
