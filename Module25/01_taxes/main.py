class Property:
    def __init__(self, worth):
        self.worth = worth

    def tax_calculate(self):
        return self.worth / 1


class Apartment(Property):

    def tax_calculate(self):
        return self.worth / 1000


class Car(Property):

    def tax_calculate(self):
        return self.worth / 200


class CountryHouse(Property):

    def tax_calculate(self):
        return self.worth / 500


def main():
    while True:
        choice = input("На какое имущество нужно вычислить налог?"
                       "\n0 - Выйти"
                       "\n1 - Квартира"
                       "\n2 - Машина"
                       "\n3 - Дача\n")
        if choice == "0":
            break
        price = float(input("Введите стоимость: "))
        if choice == "1":
            apartment = Apartment(price)
            print("\nНалог = {}\n".format(
                apartment.tax_calculate()
            ))
        elif choice == "2":
            car = Car(price)
            print("\nНалог = {}\n".format(
                car.tax_calculate()
            ))
        elif choice == "3":
            country_house = CountryHouse(price)
            print("\nНалог = {}\n".format(
                country_house.tax_calculate()
            ))
        else:
            print("\nОшибка ввода\n")


if __name__ == '__main__':
    main()

# зачёт! 🚀
