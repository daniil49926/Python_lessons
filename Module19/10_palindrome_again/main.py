text = input("Введите строку: ")
text_dict = dict()
for i in text:
    if i in text_dict:
        text_dict[i] += 1
    else:
        text_dict[i] = 1
print(text_dict)

count = 0

for i in text_dict:
    if text_dict[i] % 2 != 0:
        count += 1
if count >= 2:
    print("Нельзя сделать палиндромом")
else:
    print("Можно сделать палиндромом")

# зачёт! 🚀
