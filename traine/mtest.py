import math


def my_func(in_dict: dict) -> dict:
    out_dict = dict()
    try:
        for key, val in in_dict.items():
            val = math.ceil(val * 1.15)
            while val % 5 != 0:
                val += 1
            out_dict[key] = val
    except AttributeError:
        print("Ошибка формата ввода")
    return out_dict


input_dict = {
    "apple": 800,
    "banana": 600,
    "milk": 700
}

print(my_func(input_dict))

