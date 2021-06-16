import os

input_file = open(os.path.abspath("zen.txt"), "r", encoding="UTF-8")
num_line = 0
num_word = 0
num_sign = 0
list_exs = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f",
            "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

dict_sign = dict()

for i_line in input_file:
    for i_sign in i_line:
        if i_sign.lower() in list_exs:
            num_sign += 1
            if i_sign in dict_sign:
                dict_sign[i_sign.lower()] += 1
            else:
                dict_sign[i_sign.lower()] = 1
    num_word += len(i_line.split())
    num_line += 1
print(f"Кол-во строк - {num_line}\n"
      f"Кол-во слов - {num_word}\n"  
      f"Кол-во букв - {num_sign - 18}\n")  # 18 - кол-во литералов \n
input_file.close()

print("Буква которая встречается в тексте наименьшее количество раз")
min_val = (min(dict_sign.values()))
for key, val in dict_sign.items():
    if val == min_val:
        print(f"'{key}' - {val}")

# зачёт! 🚀
