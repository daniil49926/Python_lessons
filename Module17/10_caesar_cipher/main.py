def cipher(line, shift):
    new_text = ""
    count_list = [(alphabet[(alphabet.index(i) + shift) % 33] if i != " " else " ") for i in line]
    for i in count_list:
        new_text += i
    return new_text


alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
text = input("Введите текст: ")
step = int(input("Введите сдвиг: "))
print(f"Расшифравка: {cipher(text, step)}")

# зачёт! 🚀
