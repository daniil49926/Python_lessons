import os


def sub_fol_weight(path):
    weight_in_func = 0
    file_in_func = 0
    sub_in_func = 0
    for i_elem in os.listdir(path):
        if os.path.isfile(os.path.join(path, i_elem)):
            file_in_func += 1
            weight_in_func += os.path.getsize(os.path.join(path, i_elem))
        else:
            sub_in_func += 1
            weight_in_func += sub_fol_weight(os.path.join(path, i_elem))[0]

    else:
        return weight_in_func, file_in_func, sub_in_func


input_path = input("Введите путь: ")
num_sub_folder = 0
num_file = 0
weight = 0
for i in os.listdir(input_path):
    if os.path.isdir(os.path.join(input_path, i)):
        num_sub_folder += 1
        weight += sub_fol_weight(os.path.join(input_path, i))[0]
        num_file += sub_fol_weight(os.path.join(input_path, i))[1]
        num_sub_folder += sub_fol_weight(os.path.join(input_path, i))[2]
    if os.path.isfile(os.path.join(input_path, i)):
        num_file += 1
        weight += os.path.getsize(os.path.join(input_path, i))
print(f"Размер каталога (в Кб) {weight/1024} ({weight} байт)\n"
      f"Кол-во подкаталогов {num_sub_folder}\n"
      f"Кол-во файлов {num_file}")

# зачёт! 🚀
