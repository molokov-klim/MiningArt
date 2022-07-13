from check_fuel import take_range, take_long_timestamps, take_tech_id, calc_fuel, take_list_timestamps


def init():
    HELP = 'exit - выход; 1 - рассчитать расход топлива; 2 - посчитать количество указанных символов в строке'
    print(HELP)
    CMD = input("Вы в главном меню. Введите команду: ")

    while CMD != "exit":
        if CMD == "1":
            print("1 - check fuel selected ")

            USER_RANGE = take_range()
            FUEL_TIMESTAMPS = take_long_timestamps(USER_RANGE)
            TECH_ID = take_tech_id(FUEL_TIMESTAMPS)
            take_list_timestamps(USER_RANGE)
            calc_fuel(FUEL_TIMESTAMPS, TECH_ID, USER_RANGE)

            # print(USER_RANGE)
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


