def read_line(line):
    count = ""
    error_str = ""
    my_operation = []
    for sign in line:
        if sign == " " or sign == "\n":
            my_operation.append(count)
            count = ""
        else:
            count += sign
    if len(my_operation) == 3:
        try:
            if my_operation[1] == "+":
                return int(my_operation[0]) + int(my_operation[2])
            elif my_operation[1] == "-":
                return int(my_operation[0]) - int(my_operation[2])
            elif my_operation[1] == "/":
                return int(my_operation[0]) / int(my_operation[2])
            elif my_operation[1] == "//":
                return int(my_operation[0]) // int(my_operation[2])
            elif my_operation[1] == "*":
                return int(my_operation[0]) * int(my_operation[2])
            elif my_operation[1] == "%":
                return int(my_operation[0]) % int(my_operation[2])
            elif my_operation[1] == "**":
                return int(my_operation[0]) ** int(my_operation[2])
            else:
                for i in my_operation:
                    error_str += f"{i} "
                choice = input(f"Обнаружена ошибка в строке {error_str}\tХотите исправить? ")
                if choice.casefold() == "да":
                    corrected_lines = input("Введите исправленную строку: ")
                    corrected_lines += "\n"
                    return read_line(corrected_lines)
                if choice.casefold() == "нет":
                    return None

        except ValueError:
            return None
    else:
        for i in my_operation:
            error_str += f"{i} "
        choice = input(f"Обнаружена ошибка в строке {error_str}\tХотите исправить? ")
        if choice.casefold() == "да":
            corrected_lines = input("Введите исправленную строку: ")
            corrected_lines += "\n"
            return read_line(corrected_lines)
        if choice.casefold() == "нет":
            return None


rez = 0
with open("calc.txt", "r") as inp_file:
    for i_line in inp_file:
        try:
            if "\n" not in i_line:
                i_line += "\n"
            rez += read_line(i_line)
        except (TypeError, ZeroDivisionError):
            pass
print(f"Ответ: {rez}")

# зачёт! 🚀
