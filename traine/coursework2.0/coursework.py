import PySimpleGUI
import mysql.connector


def connect_base():
    return mysql.connector.connect(user="", password="", host="", database="")


def user_log_in(u_login, u_password):
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute("SELECT * FROM base_table_user")
    rows = cursor.fetchall()
    for elem in rows:
        if elem[1] == u_login and elem[2] == u_password:
            user_choice_object(elem[1])
    c_base.commit()
    c_base.close()
    c_base.close()


def user_choice_object(user_name):
    main_layout = [
        [PySimpleGUI.Text(size=(0, 1))],
        [PySimpleGUI.Text("Добро пожаловать, {}".format(
            user_name
        ), size=(50, 2), font="Courier 18")],
        [PySimpleGUI.Text(size=(0, 2))],
        [PySimpleGUI.Text("Выберите предмет:", size=(50, 2), font="Courier 16", text_color="#333333")],
        [PySimpleGUI.Text(size=(0, 2))],
        [PySimpleGUI.Button("Математика", key="math", size=(15, 1), button_color="green"),
         PySimpleGUI.Button("Программирование", key="prog", size=(15, 1), button_color="red"),
         PySimpleGUI.Button("Физика", key="physics", size=(15, 1), button_color="grey"),
         PySimpleGUI.Button("Английский", key="english", size=(15, 1), button_color="purple")]]

    main_window = PySimpleGUI.Window("Выбор предмета", main_layout, size=(1024, 500))

    while True:
        event, values = main_window.read()
        if event == PySimpleGUI.WINDOW_CLOSED:
            main_window.close()
            break
        if event == "math":
            main_window.close()
            user_inter_math(user_name, "math")
            break

        if event == "prog":
            main_window.close()
            user_inter_prog(user_name, "prog")
            break

        if event == "physics":
            main_window.close()
            user_inter_phy(user_name, "phy")
            break

        if event == "english":
            main_window.close()
            user_inter_engl(user_name, "engl")
            break


def user_inter_engl(user_name, object):
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"SELECT link_homework_engl FROM base_table_user WHERE name = '{user_name}'")
    rows = cursor.fetchall()
    link = rows[0][0]
    c_base.commit()
    c_base.close()
    c_base.close()
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"SELECT score FROM base_table_user WHERE name = '{user_name}'")
    rows = cursor.fetchall()
    score = rows[0][0]
    c_base.commit()
    c_base.close()
    c_base.close()
    info = ""
    if score <= 52:
        info = "Надо поднажать, итоговая оценка за семестр = 2"
    elif score <= 73:
        info = "Зачет уже есть, но можно и повысить оценку"
    elif score <= 94:
        info = "Итоговая оценка = 4"
    elif score > 94:
        info = "Отличная работа, оценка за семестр 5"
    main_layout = [
        [PySimpleGUI.Button("Назад", key="back", size=(10, 1), button_color="light grey")],
        [PySimpleGUI.Text(size=(0, 1))],
        [PySimpleGUI.Text("Предмет - английский язык", size=(50, 2), font="Courier 18")],
        [PySimpleGUI.Text("Ваш прогресс - {}    {}".format(
            score,
            info
        ))],
        [PySimpleGUI.Text("Новое домашнее задание по данному предмету - {}".format(
            link
        ))],
        [PySimpleGUI.Text("Добавить ответ", size=(40, 1))],
        [PySimpleGUI.Input(key="link_answer", size=(30, 1))],
        [PySimpleGUI.Button("Добавить ответ", key="add_answer", size=(15, 1))]]

    main_window = PySimpleGUI.Window("Основное окно", main_layout, size=(1024, 500))

    while True:
        event, values = main_window.read()
        if event == PySimpleGUI.WINDOW_CLOSED:
            main_window.close()
            break

        if event == "back":
            main_window.close()
            user_choice_object(user_name)

        if event == "add_answer":
            answer_link = str(values["link_answer"])
            add_answer(user_name, answer_link, object)
            main_window.close()
            user_inter_math(user_name, object)
            break


def user_inter_phy(user_name, object):
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"SELECT link_homework_phy FROM base_table_user WHERE name = '{user_name}'")
    rows = cursor.fetchall()
    link = rows[0][0]
    c_base.commit()
    c_base.close()
    c_base.close()
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"SELECT score FROM base_table_user WHERE name = '{user_name}'")
    rows = cursor.fetchall()
    score = rows[0][0]
    c_base.commit()
    c_base.close()
    c_base.close()
    info = ""
    if score <= 52:
        info = "Надо поднажать, итоговая оценка за семестр = 2"
    elif score <= 73:
        info = "Зачет уже есть, но можно и повысить оценку"
    elif score <= 94:
        info = "Итоговая оценка = 4"
    elif score > 94:
        info = "Отличная работа, оценка за семестр 5"
    main_layout = [
        [PySimpleGUI.Button("Назад", key="back", size=(10, 1), button_color="light grey")],
        [PySimpleGUI.Text(size=(0, 1))],
        [PySimpleGUI.Text("Предмет - физика", size=(50, 2), font="Courier 18")],
        [PySimpleGUI.Text("Ваш прогресс - {}    {}".format(
            score,
            info
        ))],
        [PySimpleGUI.Text("Новое домашнее задание по данному предмету - {}".format(
            link
        ))],
        [PySimpleGUI.Text("Добавить ответ", size=(40, 1))],
        [PySimpleGUI.Input(key="link_answer", size=(30, 1))],
        [PySimpleGUI.Button("Добавить ответ", key="add_answer", size=(15, 1))]]

    main_window = PySimpleGUI.Window("Основное окно", main_layout, size=(1024, 500))

    while True:
        event, values = main_window.read()
        if event == PySimpleGUI.WINDOW_CLOSED:
            main_window.close()
            break

        if event == "back":
            main_window.close()
            user_choice_object(user_name)

        if event == "add_answer":
            answer_link = str(values["link_answer"])
            add_answer(user_name, answer_link, object)
            main_window.close()
            user_inter_math(user_name, object)
            break


def user_inter_prog(user_name, object):
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"SELECT link_homework_prog FROM base_table_user WHERE name = '{user_name}'")
    rows = cursor.fetchall()
    link = rows[0][0]
    c_base.commit()
    c_base.close()
    c_base.close()
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"SELECT score FROM base_table_user WHERE name = '{user_name}'")
    rows = cursor.fetchall()
    score = rows[0][0]
    c_base.commit()
    c_base.close()
    c_base.close()
    info = ""
    if score <= 52:
        info = "Надо поднажать, итоговая оценка за семестр = 2"
    elif score <= 73:
        info = "Зачет уже есть, но можно и повысить оценку"
    elif score <= 94:
        info = "Итоговая оценка = 4"
    elif score > 94:
        info = "Отличная работа, оценка за семестр 5"
    main_layout = [
        [PySimpleGUI.Button("Назад", key="back", size=(10, 1), button_color="light grey")],
        [PySimpleGUI.Text(size=(0, 1))],
        [PySimpleGUI.Text("Предмет - программирование", size=(50, 2), font="Courier 18")],
        [PySimpleGUI.Text("Ваш прогресс - {}    {}".format(
            score,
            info
        ))],
        [PySimpleGUI.Text("Новое домашнее задание по данному предмету - {}".format(
            link
        ))],
        [PySimpleGUI.Text("Добавить ответ", size=(40, 1))],
        [PySimpleGUI.Input(key="link_answer", size=(30, 1))],
        [PySimpleGUI.Button("Добавить ответ", key="add_answer", size=(15, 1))]]

    main_window = PySimpleGUI.Window("Основное окно", main_layout, size=(1024, 500))

    while True:
        event, values = main_window.read()
        if event == PySimpleGUI.WINDOW_CLOSED:
            main_window.close()
            break

        if event == "back":
            main_window.close()
            user_choice_object(user_name)

        if event == "add_answer":
            answer_link = str(values["link_answer"])
            add_answer(user_name, answer_link, object)
            main_window.close()
            user_inter_math(user_name, object)
            break


def user_inter_math(user_name, object):
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"SELECT link_homework_math FROM base_table_user WHERE name = '{user_name}'")
    rows = cursor.fetchall()
    link = rows[0][0]
    c_base.commit()
    c_base.close()
    c_base.close()
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"SELECT score FROM base_table_user WHERE name = '{user_name}'")
    rows = cursor.fetchall()
    score = rows[0][0]
    c_base.commit()
    c_base.close()
    c_base.close()
    info = ""
    if score <= 52:
        info = "Надо поднажать, итоговая оценка за семестр = 2"
    elif score <= 73:
        info = "Зачет уже есть, но можно и повысить оценку"
    elif score <= 94:
        info = "Итоговая оценка = 4"
    elif score > 94:
        info = "Отличная работа, оценка за семестр 5"
    main_layout = [
        [PySimpleGUI.Button("Назад", key="back", size=(10, 1), button_color="light grey")],
        [PySimpleGUI.Text(size=(0, 1))],
        [PySimpleGUI.Text("Предмет - математика", size=(50, 2), font="Courier 18")],
        [PySimpleGUI.Text("Ваш прогресс - {}    {}".format(
            score,
            info
        ))],
        [PySimpleGUI.Text("Новое домашнее задание по данному предмету - {}".format(
            link
        ))],
        [PySimpleGUI.Text("Добавить ответ", size=(40, 1))],
        [PySimpleGUI.Input(key="link_answer", size=(30, 1))],
        [PySimpleGUI.Button("Добавить ответ", key="add_answer", size=(15, 1))]]

    main_window = PySimpleGUI.Window("Основное окно", main_layout, size=(1024, 500))

    while True:
        event, values = main_window.read()
        if event == PySimpleGUI.WINDOW_CLOSED:
            main_window.close()
            break

        if event == "back":
            main_window.close()
            user_choice_object(user_name)

        if event == "add_answer":
            answer_link = str(values["link_answer"])
            add_answer(user_name, answer_link, object)
            main_window.close()
            user_inter_math(user_name, object)
            break


def add_answer(name, answer, object):
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"UPDATE base_table_user SET link_answer_{object} = '{answer}' WHERE name = '{name}' ")
    c_base.commit()
    c_base.close()
    c_base.close()
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"UPDATE base_table_user SET link_homework_{object} = '' WHERE name = '{name}' ")
    c_base.commit()
    c_base.close()
    c_base.close()


def teacher_log_in(t_login, t_password):
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute("SELECT * FROM base_table_admin")
    rows = cursor.fetchall()
    for elem in rows:
        if elem[1] == t_login and elem[2] == t_password:
            teacher_inter(elem[1], elem[3])
    c_base.commit()
    c_base.close()
    c_base.close()


def teacher_inter(teach_name, role):
    view_user_progress = ""
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute("SELECT * FROM base_table_user")
    rows = cursor.fetchall()
    if role == "math":
        number = 4
    if role == "prog":
        number = 6
    if role == "phy":
        number = 8
    if role == "engl":
        number = 10
    for elem in rows:
        view_user_progress += f"Имя пользователя - {elem[1]}\n" \
                              f"Ответ на домашнее задание - {elem[number]}\n" \
                              f"Текущий прогресс - {elem[5]}\n"
    c_base.commit()
    c_base.close()
    c_base.close()
    user_progress = [[PySimpleGUI.Text(view_user_progress)]]
    obj = ""
    if role == "math":
        obj = "Математика"
    if role == "prog":
        obj = "Программирование"
    if role == "phy":
        obj = "Физика"
    if role == "engl":
        obj = "Английский язык"
    main_layout = [
        [PySimpleGUI.Text(size=(0, 1))],
        [PySimpleGUI.Button("Назад", key="back", size=(10, 1), button_color="light grey")],
        [PySimpleGUI.Text(f"Комната {obj}", size=(50, 1))],
        [PySimpleGUI.Text("Добро пожаловать, {}".format(
            teach_name
        ), size=(50, 2), font="Courier 18")],
        [PySimpleGUI.Text("Прогресс пользователей", size=(60, 1), font="Courier 28", text_color="black")],
        [PySimpleGUI.Column(user_progress, size=(1000, 200), scrollable=True, key="user_progress")],
        [PySimpleGUI.Text("Засчитать работу", size=(60, 1), font="Courier 28", text_color="black")],
        [PySimpleGUI.Text("Пользователь", size=(28, 1)), PySimpleGUI.Text("Кол-во баллов за работу", size=(25, 1))],
        [PySimpleGUI.Input(key="selected_user", size=(30, 1)),
         PySimpleGUI.Input(key="score+", size=(25, 1)),
         PySimpleGUI.Button("Засчитать работу", key="add_score", size=(15, 1))],
        [PySimpleGUI.Text("Добавить работу", size=(60, 1), font="Courier 28", text_color="black")],
        [PySimpleGUI.Text("Пользователь", size=(28, 1)), PySimpleGUI.Text("Ссылка на работу", size=(25, 1))],
        [PySimpleGUI.Input(key="selected_user_add", size=(30, 1)),
         PySimpleGUI.Input(key="homework", size=(25, 1)),
         PySimpleGUI.Button("Добавить работу", key="add_homework", size=(15, 1))]]

    main_window = PySimpleGUI.Window("Основное окно", main_layout, size=(1024, 800))

    while True:
        event, values = main_window.read()
        if event == PySimpleGUI.WINDOW_CLOSED:
            main_window.close()
            break

        if event == "back":
            main_window.close()
            login()
            break

        if event == "add_score":
            user_name = str(values["selected_user"])
            user_score = int(values["score+"])
            add_score(user_name, user_score, role)
            main_window.close()
            teacher_inter(teach_name, role)
            break

        if event == "add_homework":
            user_name = str(values["selected_user_add"])
            user_homework = str(values["homework"])
            add_homework(user_name, user_homework, role)
            main_window.close()
            teacher_inter(teach_name, role)
            break


def add_homework(name, homework, role):
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"UPDATE base_table_user SET link_homework_{role} = '{homework}' WHERE name = '{name}' ")
    c_base.commit()
    c_base.close()
    c_base.close()


def add_score(name, score, role):
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"UPDATE base_table_user SET score = score + {score} WHERE name = '{name}' ")
    c_base.commit()
    c_base.close()
    c_base.close()
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"UPDATE base_table_user SET link_answer_{role} = '' WHERE name = '{name}' ")
    c_base.commit()
    c_base.close()
    c_base.close()


def log_on():
    main_layout = [
        [PySimpleGUI.Text(size=(0, 5))],
        [PySimpleGUI.Text(size=(43, 0)), PySimpleGUI.Text("Введите логин и пароль", size=(50, 2))],
        [PySimpleGUI.Text(size=(43, 0)), PySimpleGUI.Text("Доступная роль: Пользователь", size=(50, 2))],
        [PySimpleGUI.Text(size=(43, 0)), PySimpleGUI.Input(key="name", size=(30, 1))],
        [PySimpleGUI.Text(size=(43, 0)), PySimpleGUI.Input(key="password", size=(30, 1))],
        [PySimpleGUI.Text(size=(20, 0)),
         PySimpleGUI.Button("Зарегистрироваться", key="log-on", size=(15, 1), button_color="light grey")]]

    main_window = PySimpleGUI.Window("Вход", main_layout, size=(1024, 500))

    while True:
        event, values = main_window.read()
        if event == PySimpleGUI.WINDOW_CLOSED:
            main_window.close()
            break
        if event == "log-on":
            user_login = str(values["name"])
            user_password = str(values["password"])
            add_users(user_login, user_password)
            main_window.close()
            break


def add_users(log, passw):
    c_base = connect_base()
    cursor = c_base.cursor()
    cursor.execute(f"""
    INSERT INTO `base_table_user` 
    (`id`, `name`, `password`, `link_homework_math`, `link_answer_math`, 
    `link_homework_prog`, `link_answer_prog`, 
    `link_homework_phy`, `link_answer_phy`, 
    `link_homework_engl`, `link_answer_engl`, `score`) 
    VALUES 
    (NULL, '{log}', '{passw}', '', '', '', '', '', '', '', '', '0')
    """)
    c_base.commit()
    c_base.close()
    c_base.close()
    login()


def login():
    main_layout = [
        [PySimpleGUI.Text(size=(0, 5))],
        [PySimpleGUI.Text(size=(43, 0)), PySimpleGUI.Text("Вход в систему", size=(50, 2))],
        [PySimpleGUI.Text(size=(43, 0)), PySimpleGUI.Input(key="name", size=(30, 1))],
        [PySimpleGUI.Text(size=(43, 0)), PySimpleGUI.Input(key="password", size=(30, 1))],
        [PySimpleGUI.Text(size=(40, 0)), PySimpleGUI.Button("Войти как ученик", key="user_log-in", size=(15, 1)),
         PySimpleGUI.Button("Войти как учитель", key="teacher_log-in", size=(15, 1))],
        [PySimpleGUI.Text(size=(49, 0)),
         PySimpleGUI.Button("Регистрация", key="log-on", size=(15, 1), button_color="light grey")]]

    main_window = PySimpleGUI.Window("Вход", main_layout, size=(1024, 500))

    while True:
        event, values = main_window.read()
        if event == PySimpleGUI.WINDOW_CLOSED:
            main_window.close()
            break
        if event == "user_log-in":
            user_login = str(values["name"])
            user_password = str(values["password"])
            main_window.close()
            user_log_in(user_login, user_password)
            break
        if event == "teacher_log-in":
            teacher_login = str(values["name"])
            teacher_password = str(values["password"])
            main_window.close()
            teacher_log_in(teacher_login, teacher_password)
            break

        if event == "log-on":
            log_on()
            main_window.close()
            break


if __name__ == '__main__':
    PySimpleGUI.theme("Reddit")
    login()