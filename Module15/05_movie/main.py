def list_movie(film, list_films):
    return film in list_films


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

films_list = []
while True:
    print(f"Ваш список на данный момент:\n{films_list}")
    new_film = input("Введите фильм(для выхода введите 'end'): ")
    if new_film == "end":
        break
    if list_movie(new_film, films):
        if not list_movie(new_film, films_list):
            films_list.append(new_film)
        else:
            print("Вы уже добавляли такой фильм")
    else:
        print("Такого фильма у нас нет.")

print(f"Фильмы которые вы добавили в избранное\n{films_list}")

# зачёт! 🚀
