import os
import zipfile

input_zip = zipfile.ZipFile("voyna-i-mir.zip", mode="r")
input_zip.extract("voyna-i-mir.txt", os.path.abspath("voyna-i-mir"))
input_zip.close()

my_dict = dict()

input_file = open(os.path.abspath(os.path.join("voyna-i-mir", "voyna-i-mir.txt")), encoding="UTF-8")

for i_line in input_file:
    for i_sign in i_line:
        if i_sign not in my_dict:
            my_dict[i_sign] = 1
        else:
            my_dict[i_sign] += 1
del my_dict["\n"]
print(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

# зачёт! 🚀
