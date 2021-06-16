def search_city(str_dict, str_city):
    for i_list in str_dict:
        for i in range(len(str_dict[i_list])):
            if str_dict[i_list][i] == str_city:
                return i_list
    return False


def main():
    num_of_country = int(input("Введите кол-во стран: "))
    city_dict = {}

    for i in range(num_of_country):
        city = input(f"{i + 1} страна: ").split()
        city_dict[city[0]] = city[1:]

    for j in range(3):
        city = input("Введите {number} город: ".format(
            number=(j + 1)
        ))
        country = search_city(city_dict, city)
        if not country:
            print("По городу {city} нет информации".format(
                city=city
            ))
        else:
            print(f"Город {city} расположен в стране {country}.".format(
                city=city,
                country=country
            ))


main()

# зачёт! 🚀
