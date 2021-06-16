numbers = int(input("Введите кол-во чисел в списке: "))
score_list = []
for i in range(numbers):
    score = int(input(f"Введите кол-во очков бегуна {i + 1}: "))
    score_list.append(score)

print(score_list)
maximum = score_list[0]
minimum = score_list[0]
count_max = 0
count_min = 0

for i in range(numbers):
    if score_list[i] > maximum:
        maximum = score_list[i]
        count_max = i
    if score_list[i] < minimum:
        minimum = score_list[i]
        count_min = i

score_list[count_min], score_list[count_max] = score_list[count_max], score_list[count_min]
print(score_list)
