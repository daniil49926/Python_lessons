text = input("Введите текст:\n")
text_list = list(text)
sym = input("Введите символ: ")
new_sym = input("Введите на что заменить: ")
print("Новый текст:\n")
count = 0
for i in text_list:
    if i == sym:
        text_list[count] = new_sym
    print(text_list[count], end="")
    count += 1