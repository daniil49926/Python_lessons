import random

first_team = [round(random.uniform(5, 10), 2) for i in range(20)]
second_team = [round(random.uniform(5, 10), 2) for i in range(20)]
win_team = [first_team[i] if first_team[i] > second_team[i]
            else second_team[i] for i in range(20)]
print(f"Первая команда: {first_team}\n"
      f"Вторая команда: {second_team}\n"
      f"Победители тура: {win_team}")

# зачёт! 🚀
