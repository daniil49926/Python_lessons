text = input("Введите текст: ").split()
for word in enumerate(text):
    print(word[0] + 1, word[1][:10])
