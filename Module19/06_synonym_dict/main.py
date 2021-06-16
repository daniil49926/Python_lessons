def syn_dict():
    num_of_word = int(input("Введите кол-во слов: "))
    synonym_dict = dict()
    reverse_dict = dict()

    for i in range(num_of_word):
        word_and_synonym = input(f"{i + 1} пара: ").split(" - ")
        synonym_dict[word_and_synonym[0]] = word_and_synonym[1]
        reverse_dict[word_and_synonym[1]] = word_and_synonym[0]

    while True:
        word = input("Введите слово\nДля выхода введите 'end'\n")
        if word == "end":
            break
        else:
            answer = "такого слова не найден."
            print(f"Синоним {synonym_dict.get(word, reverse_dict.get(word, answer))}")


syn_dict()

# зачёт! 🚀
