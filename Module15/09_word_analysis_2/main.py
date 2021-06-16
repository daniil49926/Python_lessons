word = input("Введите слово: ")
list_word = list(word)
count = 0
for i in range(len(list_word)):
    if list_word[i] == list_word[-(i + 1)]:
        count += 1
if count == len(list_word):
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")

# зачёт! 🚀
