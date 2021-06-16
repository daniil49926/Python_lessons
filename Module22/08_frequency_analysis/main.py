import os


permitted_sign = "qwertyuiopasdfghjklzxcvbnm"
rez_dict = dict()
input_file = open(os.path.abspath("text.txt"), "r", encoding="UTF-8")
for i_line in input_file:
    for i_sign in i_line.lower():
        if i_sign in permitted_sign:
            rez_dict[i_sign] = i_line.lower().count(i_sign)

sum_dict = 0
for i in rez_dict:
    sum_dict += int(rez_dict[i])
output_file = open(os.path.abspath("analysis.txt"), "w", encoding="UTF-8")
for j in rez_dict:
    rez_dict[j] = round((rez_dict[j] / sum_dict), 3)
    output_file.write((str(j) + " " + str(rez_dict[j]) + "\n"))
output_file.close()

# зачёт! 🚀
