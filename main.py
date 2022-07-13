from check_fuel import take_range, take_timestamps, take_tech_id, calc_fuel


def init():
    HELP = 'exit - выход; 1 - рассчитать расход топлива; 2 - посчитать количество указанных символов в строке'
    print(HELP)
    CMD = input("Вы в главном меню. Введите команду: ")

    while CMD != "exit":
        if CMD == "1":
            print("1 - check fuel selected ")

            USER_RANGE = take_range()
            FUEL_TIMESTAMPS = take_timestamps(USER_RANGE)
            TECH_ID = take_tech_id(FUEL_TIMESTAMPS)
            calc_fuel(FUEL_TIMESTAMPS, TECH_ID)

            print(USER_RANGE)
            # print(FUEL_TIMESTAMPS)
            # print(TECH_ID)

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


