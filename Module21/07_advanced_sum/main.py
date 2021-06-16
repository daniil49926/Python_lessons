def summa(*args, new_list=None):
    rez = 0
    args = list(args)
    if new_list is None:
        new_list = [args]
    for i in new_list:
        if type(i) != int:
            new_list.remove(i)
            new_list.extend(i)
        else:
            new_list.remove(i)
            new_list.append(i)
    for i in new_list:
        if type(i) != int:
            return summa(new_list=new_list)
    else:
        for i in new_list:
            rez += i
        return rez


print(summa([1, [[[[[[2], [[[3]]]]]]], [4]]], [[[[[5], 6]]], [9]]))

# зачёт! 🚀
