vowels = "аоуыэеёюяи"
text = input("Введите текст: ")
list_vowels = [i for i in text if i in vowels]
print(f"\nСписок гласных: {list_vowels}\nДлина списка: {len(list_vowels)}")

# зачёт! 🚀
