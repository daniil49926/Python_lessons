good_rez = ""
bad_rez = ""
line_count = 0
with open("registrations.txt", "r", encoding="UTF-8") as inp_file:
    for i_line in inp_file:
        line_count += 1
        count = ""
        line_list = []
        for sign in i_line:
            if sign == " " or sign == "\n":
                line_list.append(count)
                count = ""
            else:
                count += sign
        if len(line_list) == 3:
            if line_list[0].isalpha():
                if "@" in line_list[1] or "." in line_list[1]:
                    if 10 <= int(line_list[2]) <= 99:
                        good_rez += f"{i_line}"
                    else:
                        bad_rez += f"ValueError: {line_count}: {i_line}"
                else:
                    bad_rez += f"SyntaxError: {line_count}: {i_line}"
            else:
                bad_rez += f"NameError: {line_count}: {i_line}"
        else:
            bad_rez += f"ValueError: {line_count}: {i_line}"

        with open("registrations_good.log", "w", encoding="UTF-8") as file_good:
            file_good.write(good_rez)
        with open("registrations_bad.log", "w", encoding="UTF-8") as file_bad:
            file_bad.write(bad_rez)

# зачёт! 🚀
