def search(name, shop_list):
    summa = 0
    count = 0
    for i in range(len(shop_list)):
        for j in range(2):
            if name == shop_list[i][j]:
                count += 1
                summa += shop_list[i][j + 1]
    print(f"\nКол-во деталей - {count}\nОбщая стоимость - {summa}\n")


def main():
    shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
            ['педаль', 100], ['седло', 1500], ['рама', 12000],
            ['обод', 2000], ['шатун', 200], ['седло', 2700]]

    answer = input("Введите название: ")
    search(answer, shop)
    main()


main()

# зачёт! 🚀
