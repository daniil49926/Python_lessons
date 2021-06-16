import os
from collections.abc import Iterable


def gen_files_path(inp_path: str, inp_start_path: str) -> Iterable[str]:
    for dirpath, dirnames, filenames in os.walk(inp_start_path):
        for dirname in dirnames:
            yield f"Каталог: {os.path.join(dirpath, dirname)}"
            if inp_path in os.path.join(dirpath, dirname):
                print("Каталог найден")
                return
        for filename in filenames:
            yield f"Файл: {os.path.join(dirpath, filename)}"
            if inp_path in os.path.join(dirpath, filename):
                print("Файл найден")
                return


path = input("Введите папку/файл который ищем: ")
start_path = input("Введите директорию в которой ищем: ")

for i in gen_files_path(path, start_path):
    print(i)

# зачёт! 🚀
