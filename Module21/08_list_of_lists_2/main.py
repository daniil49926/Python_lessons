nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def easy_list(new_list):
    for i in new_list:
        if type(i) != int:
            new_list.remove(i)
            new_list.extend(i)
        else:
            new_list.remove(i)
            new_list.append(i)
    for i in new_list:
        if type(i) != int:
            return easy_list(new_list=new_list)
    else:
        return list(set(new_list))


print(easy_list(nice_list))

# зачёт! 🚀
