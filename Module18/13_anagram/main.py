first_word = list(input("Первое слово: "))
second_word = list(input("Второе слово: "))
if sorted(first_word) == sorted(second_word):
    print("Слова являются анаграммами друг друга")
else:
    print("Слова не являются анаграммами друг друга")

# зачёт! 🚀
