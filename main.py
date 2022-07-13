from check_fuel import show_max_range


def init():
    HELP = 'exit - close program; 1 - check fuel; 2 - find character; 0 - settings'
    print(HELP)
    CMD = input("Вы в главном меню. Введите команду: ")

    while CMD != "exit":
        if CMD == "1":
            print("1 - check fuel selected ")
            show_max_range()

        elif CMD == "2":
            print("2 - find character selected ")
            #find_character()

        elif CMD == "":
            print("Введенной команды не существует")
            print(HELP)

        else:
            print("Введенной команды не существует")
            print(HELP)

        CMD = input("Вы в главном меню. Введите команду: ")

    return
            

if __name__ == '__main__':
    init()


