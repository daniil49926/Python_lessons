import os


count = 0
k = None
rez_dict = dict()
input_file = open(os.path.abspath("first_tour.txt"), "r", encoding="UTF-8")

for i_line in input_file:
    if k is None:
        k = int(i_line)
    else:
        first_part, second_part, third_part = i_line.split()
        if int(third_part) > k:
            rez_dict[second_part[0] + ". " + first_part] = third_part
input_file.close()

sort_val = sorted(rez_dict.values())[::-1]
rez_sort_dict = dict()
for i in sort_val:
    for j in rez_dict.keys():
        if rez_dict[j] == i:
            rez_sort_dict[j] = rez_dict[j]
            break

if os.path.exists(os.path.abspath("second_tour.txt")):
    output_file = open(os.path.abspath("second_tour.txt"), "w", encoding="UTF-8")
    output_file.write("")
    output_file.close()

output_file = open(os.path.abspath("second_tour.txt"), "a", encoding="UTF-8")
output_file.write(str(len(rez_sort_dict))+"\n")
rez_sort_list = list(rez_sort_dict)
for i in range(len(rez_sort_dict)):
    output_file.write("{}) {} {}\n".format(
        i + 1,
        rez_sort_list[i],
        rez_sort_dict[rez_sort_list[i]]
    ))
output_file.close()

# зачёт! 🚀
