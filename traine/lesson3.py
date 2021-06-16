company_member = []
number_member = int(input("Введите кол-во сотрудников на работе: "))
flag = bool(True)
for i in range(number_member):
    id_member = int(input(f"ID {i + 1} -ого сотрудника: "))
    company_member.append(id_member)

print("Сотрудники в офисе:\n", company_member)

search_member = int(input("Введите ID сотрудника, которого ищите: "))

for i in range(number_member):
    if search_member == company_member[i]:
        print("Сотрудник с таким id а месте.")
        flag = False
if flag:
    print("Такого сотрудника нет в офисе.")

