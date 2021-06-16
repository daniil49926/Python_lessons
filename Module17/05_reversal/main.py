text = input("Введите текст: ")
start = text[:text.index("h")]
stop = text[len(text) - text[::-1].index("h"):]
reverse = text[len(text) - text[::-1].index("h") - 1:text.index("h") - 1:-1]
print(f"{start + reverse + stop}")

# зачёт! 🚀
