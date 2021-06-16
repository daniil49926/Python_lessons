text = input("Введите строку: ")
buff = 1
cipher = ""
x = 1
j = text[x:x+1]
for i in text:
    if i in j:
        buff += 1
    else:
        cipher += i + str(buff)
        buff = 1
    x += 1
    j = text[x:x+1]
print("Шифр:", cipher)

# зачёт! 🚀
