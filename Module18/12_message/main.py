def reverse_word(text):
    j = 0
    new_message = ""
    k = 0
    for i in range(len(text)):  # так тоже можно
        k = i
        if text[i].isalpha():
            continue
        else:
            if j == 0:
                new_message += text[k - 1::-1]          # Не очень красивый костыль,
                new_message += text[k]                  # но без него теряется первая буква
            else:
                new_message += text[k-1:j:-1]
                new_message += text[k]

            j = i

    new_message += text[k:j:-1]
    return new_message


message = input("Сообщение: ")
print("Новое сообщение {reverse_message}".format(
    reverse_message=reverse_word(message)
))

# зачёт! 🚀
