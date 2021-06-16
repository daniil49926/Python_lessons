def list_movie(film, list_films):
    for i in range(len(list_films)):
        if film == list_films[i]:
            return True
    return False


films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

films_list = []
while True:
    print(films_list)
    new_film = input("Введите фильм: ")
    if list_movie(new_film, films):
        print("Что сделать с фильмом: добавить/удалить/вставить")
        choice = input()
        if choice == "добавить":
            films_list.append(new_film)
        if choice == "удалить":
            if list_movie(new_film, films_list):
                films_list.remove(new_film)
            else:
                print("Такого фильма нет в вашем списке.")
        if choice == "вставить":
            index = int(input("На какое место поставить: "))
            films_list.insert(index - 1, new_film)
    else:
        print("Такого фильма у нас нет.")