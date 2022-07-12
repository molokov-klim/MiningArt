import psycopg2
from config import host, user, password, db_name
from check_fuel import check_fuel


def init():
    help = 'exit - close program; 1 - check fuel; 2 - find character; 0 - settings'
    print(help)
    cmd = input("Вы в главном меню. Введите команду: ")

    while cmd != "exit":
        if cmd == "1":
            print("1 - check fuel selected ")
            check_fuel()

        elif cmd == "2":
            print("2 - find character selected ")
            #find_character()

        elif cmd == "":
            print("Введенной команды не существует")
            print(help)

        else:
            print("Введенной команды не существует")
            print(help)

        cmd = input("Вы в главном меню. Введите команду: ")

    return
            

if __name__ == '__main__':
    init()


