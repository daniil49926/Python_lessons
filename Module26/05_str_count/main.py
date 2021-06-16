import os
from collections.abc import Iterable


def gen_files_path(inp_path: str) -> Iterable[int]:
    total_line = 0
    for dir_path, _, filenames in os.walk(inp_path):
        for filename in filenames:
            if os.path.join(dir_path, filename)[-3:] == ".py":
                file = open(os.path.join(dir_path, filename))
                for row in file:
                    if "#" in row:
                        continue
                    if len(row) < 2:
                        if row == "\n":
                            continue
                    total_line += 1
                file.close()
                yield total_line
                total_line = 0


path = input()
my_sum = 0
for i in gen_files_path(path):
    print(i)
    my_sum += i
print("Всего строк кода {}".format(
    my_sum
))

# зачёт! 🚀
