def sort_tuple(this_tuple):
    this_tuple = list(this_tuple)
    new_tuple = []
    for i in this_tuple:
        if type(i) != int:
            return tuple(this_tuple)
    for i in range(len(this_tuple)):
        minimum = this_tuple[0]
        for j in range(len(this_tuple)):
            if minimum > this_tuple[j]:
                minimum = this_tuple[j]
        this_tuple.remove(minimum)
        new_tuple.append(minimum)
    return tuple(new_tuple)


# NOTE альтернативный способ:
def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return tpl
    return tuple(sorted(tpl))


input_tuple = (5, 2.3, 1, 8, 2)
print(sort_tuple(input_tuple))

input_tuple = (5, 2, 1, 8, 2)
print(sort_tuple(input_tuple))

input_tuple = (5, "f", 1, 8, 2)
print(sort_tuple(input_tuple))

# зачёт! 🚀
