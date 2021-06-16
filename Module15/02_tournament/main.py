def even_index(num):
    even_list = []
    for i in range(0, len(num), 2):
        even_list.append(num[i])
    return even_list


def main():
    list_member = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    print("Список на первый день:\n", *even_index(list_member))  # так тоже можно


main()

# зачёт! 🚀
