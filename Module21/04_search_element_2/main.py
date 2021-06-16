site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search(search_key, struct, dep=None):

    while dep != 0:
        if search_key in struct:
            return struct[search_key]
        for i in struct.values():
            if isinstance(i, dict):
                if dep is None:
                    result = search(search_key, i)
                    if result:
                        break
                else:
                    result = search(search_key, i, dep - 1)
                    if result:
                        break
        else:
            result = None
        return result


key = input("Введите ключ: ")
choice = input("Нужно ли задать глубину поиска\n"
               "да/нет ")
if choice.casefold() == "да":
    depth = int(input("Введите глубину: "))
    rez = search(key, site, dep=depth)
    if rez:
        print(rez)
    else:
        print("Такого ключа нет.")
elif choice.casefold() == "нет":
    rez = search(key, site)
    if rez:
        print(rez)
    else:
        print("Такого ключа нет.")

# зачёт! 🚀
