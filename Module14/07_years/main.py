def years(start_year, stop_year):
    for i in range(start_year, stop_year + 1):
        arr = [i // 1000, (i // 100) % 10, (i // 10) % 10, i % 10]
        arr.sort()
        if (arr[0] == arr[1] and arr[0] == arr[2] and arr[0] != arr[3]) or\
                (arr[0] != arr[1] and arr[1] == arr[2] and arr[1] == arr[3]):
            print(i)


def main():
    start = int(input("Введите первый год: "))
    stop = int(input("Введите последний год: "))
    print("Года от", start, "до", stop, "с тремя одинаковыми цифрами:")
    years(start, stop)


main()