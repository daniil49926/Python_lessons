import os

input_file = open(os.path.abspath("zen.txt"), "r", encoding="UTF-8")
rez = []
for i in input_file:
    rez.append(i)
print(rez[-1])
for i in range(len(rez) - 2, 0, -1):
    print(rez[i], end="")
input_file.close()

# зачёт! 🚀
