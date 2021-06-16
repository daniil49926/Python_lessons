first_class = [i for i in range(160, 176 + 1, 2)]
second_class = [i for i in range(162, 180 + 1, 3)]
first_class.extend(second_class)
first_class.sort()
print(f"Итоговый список:\n{first_class}")

# зачёт! 🚀
