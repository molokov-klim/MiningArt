

def find_character():
    USER_STRING = input("Пожалуйста введите строку: ")
    USER_CHARACTER = input("Пожалуйста введите символ: ")

    QTY = 0
    for i in range(len(USER_STRING)):
        if USER_STRING[i]==USER_CHARACTER:
            QTY+=1
    print(f"В строке найдено {QTY} символов {USER_CHARACTER}")
