violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

rez = 0
num_of_songs = int(input("Введите кол-во песен: "))
for i in range(num_of_songs):
    name_song = input("Введите название песни: ")
    if name_song in violator_songs:
        rez += float(violator_songs[name_song])
    else:
        print("Такой песни нет в списке.")

print("Общее время звучания песен: {time} минут".format(
    time=round(rez, 2)
))

# зачёт! 🚀
