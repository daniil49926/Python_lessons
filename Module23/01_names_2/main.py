class MyException(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f"{self.text}"


rez = 0
num_lines = 1
with open("people.txt", "r") as inp_file:
    for i_line in inp_file:
        try:
            if len(i_line) < 4:
                raise MyException(f"Имя в строке {num_lines} вызвало ошибку")
            rez += len(i_line)
            if i_line.endswith("\n"):
                rez -= 1
        except MyException as err:
            print(err)

        finally:
            num_lines += 1


print(f"Результат = {rez}")

# зачёт! 🚀
