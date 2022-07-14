from check_fuel import take_range, calc_fuel, take_range_list, show_graphic
from character_finder import find_character


def init():
    HELP = 'exit - выход; 1 - рассчитать расход топлива; 2 - посчитать количество указанных символов в строке'
    print(HELP)
    CMD = input("Вы в главном меню. Введите команду: ")

    while CMD != "exit":
        if CMD == "1":
            print("1 - check fuel selected ")

            USER_RANGE = take_range() # return tuple (start_shiftdate, end_shiftdate, start_shift, end_shift, start_shiftstart_epoch, end_shiftstart_epoch)
            RANGE_LIST = take_range_list(USER_RANGE)
            calc_fuel(RANGE_LIST)

            ask_graphic = input("Отобразить на графике? (да/нет):")
            if ask_graphic == "да":
                show_graphic(USER_RANGE)
            #print(f"[SYS]USER_RANGE {USER_RANGE}")
            #print(f"[SYS]RANGE_LIST {RANGE_LIST}")

        elif CMD == "2":
            print("2 - find character selected ")
            find_character()

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


