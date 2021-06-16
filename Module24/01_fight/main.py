import random


class Warrior:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage


warrior_1 = Warrior(100, 20)
warrior_2 = Warrior(100, 20)
while True:
    if warrior_1.health <= 0:
        print("Воин 2 победил!")
        break
    if warrior_2.health <= 0:
        print("Воин 1 победил!")
        break
    rand = random.randint(1, 2)
    if rand == 1:
        warrior_2.health -= warrior_1.damage
        print("Воин 1 атаковал война 2\nЗдоровье война 2: {}\n".format(
            warrior_2.health
        ))
    else:
        warrior_1.health -= warrior_2.damage
        print("Воин 2 атаковал война 1\nЗдоровье война 1: {}\n".format(
            warrior_1.health
        ))

# зачёт! 🚀
