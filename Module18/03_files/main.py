file_name = input("Имя файла: ")
special_symbol = "@№\$%^&*()"

if file_name[0] in special_symbol:
    print("Ошибка: название начинается на один из специальных символов")
elif not file_name.endswith(".txt" or ".docx"):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
else:
    print("Файл назван верно.")

# зачёт! 🚀
