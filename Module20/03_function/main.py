def slice_tuple(inp_tuple, elem):
    flag = 0
    new_tuple = []
    for i in inp_tuple:
        if i == elem:
            flag += 1
        if flag == 1:
            new_tuple.append(i)
        elif flag == 2:
            new_tuple.append(i)
            return new_tuple
    return new_tuple


input_tuple = tuple(input("Введите кортеж: "))
sign = input("Введите элемент: ")
print("Итоговый кортеж: {0}".format(
    tuple(slice_tuple(input_tuple, sign))
))

# зачёт! 🚀
