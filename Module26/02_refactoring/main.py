from collections.abc import Iterable


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def pairwise_multiplication(first_list: list, second_list: list, find_num: int) -> Iterable[int]:
    for x in first_list:
        for y in second_list:
            result = x * y
            yield x, y, result
            if result == find_num:
                print('Found!!!')
                return


for i in pairwise_multiplication(list_1, list_2, to_find):
    print(i)

# зачёт! 🚀
