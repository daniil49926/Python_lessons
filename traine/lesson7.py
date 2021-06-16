number_pack = int(input("Введите кол-во пакетов: "))
pack = []
bad_pack = 0
revision_pack = []
for i in range(number_pack):
    pack = []
    for j in range(4):
        bit = int(input(f"{j + 1} бит: "))
        pack.append(bit)
    if pack.count(-1) > 1:
        bad_pack += 1
    else:
        revision_pack.extend(pack)

print(f"Сообщение: {revision_pack}\nПлохих пакетов: {bad_pack}")