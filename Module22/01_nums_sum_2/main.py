import os

rez = 0
input_file = open(os.path.abspath("number.txt"), "r", encoding="UTF-8")
for i_line in input_file:
    if i_line != "\n":
        rez += int(i_line)
input_file.close()
output_file = open(os.path.abspath("answer.txt"), "w", encoding="UTF-8")
output_file.write(str(rez))
output_file.close()

# зачёт! 🚀
