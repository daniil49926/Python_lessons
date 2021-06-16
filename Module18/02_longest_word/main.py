text = input("Введите текст: ").split()
maximum = ""
for i in text:
    if len(i) > len(maximum):
        maximum = i
print(f"Самое длинное слово: {maximum}\nЕго длина: {len(maximum)}")

# зачёт! 🚀
