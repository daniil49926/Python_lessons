def create_dict(string):
    text_dict = dict()
    for i in string:
        if i in text_dict:
            text_dict[i] += 1
        else:
            text_dict[i] = 1
    print("Оригинальный словарь частот:")
    for i in text_dict:
        print(i, "-", text_dict[i])
    create_fake_list(text_dict)


def create_fake_list(str_dict):
    list_text = []
    print("Инвертированный словарь частот:")
    for i in range(max(set(str_dict.values()))):
        print(i + 1, end=" : ")
        for j in str_dict:
            if str_dict[j] == i + 1:
                list_text.append(j)
        print(list_text)
        list_text.clear()


text = input("Введите текст: ").lower()
create_dict(text)

# зачёт! 🚀
