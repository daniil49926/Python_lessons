import PySimpleGUI as Psg
import random


def win_game(inp_list):
    if "1" in inp_list and "2" in inp_list and "3" in inp_list:
        return True
    if "4" in inp_list and "5" in inp_list and "6" in inp_list:
        return True
    if "7" in inp_list and "8" in inp_list and "9" in inp_list:
        return True
    if "1" in inp_list and "4" in inp_list and "7" in inp_list:
        return True
    if "2" in inp_list and "5" in inp_list and "8" in inp_list:
        return True
    if "3" in inp_list and "6" in inp_list and "9" in inp_list:
        return True
    if "1" in inp_list and "5" in inp_list and "9" in inp_list:
        return True
    if "3" in inp_list and "5" in inp_list and "7" in inp_list:
        return True
    return False


Psg.theme('Default1')
layout = [[Psg.Button(key="1", size=(5, 2)), Psg.Button(key="2", size=(5, 2)), Psg.Button(key="3", size=(5, 2))],
          [Psg.Button(key="4", size=(5, 2)), Psg.Button(key="5", size=(5, 2)), Psg.Button(key="6", size=(5, 2))],
          [Psg.Button(key="7", size=(5, 2)), Psg.Button(key="8", size=(5, 2)), Psg.Button(key="9", size=(5, 2))]]

layout_game_over = [[Psg.Text("Игра окончена", key="text_game_over", font="Arial")]]

window = Psg.Window("tic-tac-toe", layout)

list_key = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
user_list = []
computer_list = []
while True:
    event, values = window.read()
    if event == Psg.WIN_CLOSED:
        break
    if event in list_key:
        window[event].update(text="X")
        list_key.remove(event)
        user_list.append(event)
        if win_game(user_list):
            list_key.clear()
        else:
            a = random.choice(list_key)  # В данной игре компьютер будет не самый умный, тк будет выбирать рандомные
            window[a].update(text="O")  # пустые ячейки.
            list_key.remove(a)
            computer_list.append(a)
            if win_game(computer_list):
                list_key.clear()

    if len(list_key) == 0:
        window2 = Psg.Window("Game over", layout_game_over)
        event2, values2 = window2.read()
        if event2 == Psg.WIN_CLOSED:
            window2.close()
            break

window.close()

# NOTE желательно реализовать эту игру применяя средства ООП

# зачёт! 🚀
