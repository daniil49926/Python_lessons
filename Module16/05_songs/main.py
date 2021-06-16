def search(name, songs_list):
    for i in range(len(songs_list)):
        for j in range(2):
            if name == songs_list[i][j]:
                return songs_list[i][j + 1]
    print(f"Песни под названием {name} нет в нашем списке.")
    return 0


def main():
    violator_songs = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83]
    ]

    rez = 0
    number_songs = int(input("Введите кол-во песен: "))
    for i in range(number_songs):
        name_song = input(f"Введите название {i + 1} песни: ")
        rez += search(name_song, violator_songs)
    print(f"Общее время звучания песен: {round(rez, 2)} минут")


main()

# зачёт! 🚀
