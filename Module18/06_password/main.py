exitFlag = True
while True:
    password = input("Введите пароль: ")
    count = 0
    if len(password) >= 8 and not password.islower():
        for i in password:
            if i.isdigit():
                count += 1
                if count == 3:
                    print("Это надежный пароль!")
                    exitFlag = False
                    break
        else:
            print("Пароль ненадёжный. Попробуйте ещё раз.")
        if not exitFlag:
            break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")

# зачёт! 🚀
