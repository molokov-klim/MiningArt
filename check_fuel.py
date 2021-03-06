import psycopg2
from config import host, user, password, db_name, port
from graphics import show_plot


# функция указания диапазона смен
def take_range():
    try:
        # открываем соединение с базой
        connection = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as cursor:
            # запрос на минимальную дату в сменах
            cursor.execute(
                "SELECT min(shiftdate) FROM shifts"
            )

            MIN_DATE = cursor.fetchone()
            MIN_DATE = (MIN_DATE[0])

            # запрос на максимальную дату в сменах
            cursor.execute(
                "SELECT max(shiftdate) FROM shifts"
            )

            MAX_DATE = cursor.fetchone()
            MAX_DATE = MAX_DATE[0]

            # ввод пользователем даты начала интересующего его диапазона, конвертация в лист методом split и конвертация в tuple для последующего использования как переменной в запросе к psql
            INPUT_RANGE = input(
                f"Доступен временной дипазон с {MIN_DATE} по {MAX_DATE}. Пожалуйста введите дату начала и дату окончания нужного диапазона в формате 'ГГГГ-ММ-ДД ГГГГ-ММ-ДД': ")
            temp = INPUT_RANGE.split()
            USER_DATE_RANGE = (temp[0], temp[1])

            print("USER_DATE_RANGE ", type(USER_DATE_RANGE), USER_DATE_RANGE)

            # запрос смен на диапазон
            cursor.execute(
                """SELECT shiftstart, shift, crew, shiftdate, shiftstart_epoch FROM shifts WHERE shiftdate >= %s AND shiftdate <= %s""",
                (USER_DATE_RANGE[0], USER_DATE_RANGE[1])
            )
            SHIFTS_TABLE = cursor.fetchall()

            # вывод доступных смен на дату
            print("На выбранные даты доступны смены:")
            temp = 0
            for elem_tuple in SHIFTS_TABLE:
                temp += 1
                print(
                    f"Номер позиции: {temp}, дата и время начала: {elem_tuple[0]}, смена: {elem_tuple[1]}, команда: {elem_tuple[2]}")

            # ввод смен
            SHIFTS = input("Пожалуйста введите номера позиций от и до через пробел (пример '2 4'): ")
            SHIFTS = SHIFTS.split()

            USER_RANGE = (SHIFTS_TABLE[int(SHIFTS[0]) - 1][3], SHIFTS_TABLE[int(SHIFTS[1]) - 1][3],
                          SHIFTS_TABLE[int(SHIFTS[0]) - 1][1], SHIFTS_TABLE[int(SHIFTS[1]) - 1][1],
                          SHIFTS_TABLE[int(SHIFTS[0]) - 1][4], SHIFTS_TABLE[int(SHIFTS[1]) - 1][4])

            print("Выбран диапазон смен: ")
            print(
                f"Дата и смена начала: {USER_RANGE[0]}, {USER_RANGE[2]}. Дата и смена окончания: {USER_RANGE[1]}, {USER_RANGE[3]}")

            return USER_RANGE

    except Exception as _ex:
        print("[INFO] Error while working with PostrgeSQL ", _ex)

    finally:
        if connection:
            connection.close()


# формированиe списка RANGE_LIST_SHIFTS
def take_range_list(USER_RANGE):
    try:
        # открываем соединение с базой
        connection = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as cursor:
            # запрос на timestamp начала диапазона
            cursor.execute(
                """SELECT shiftdate, shift, shiftstart_epoch FROM shifts WHERE shiftstart_epoch >= %s AND shiftstart_epoch <= %s""",
                (USER_RANGE[4], USER_RANGE[5])
            )

            RANGE_LIST = cursor.fetchall()

            RANGE_LIST_LITERS_ARRAY = take_liters(RANGE_LIST)

            for i in range(len(RANGE_LIST)):
                RANGE_LIST[i] = RANGE_LIST[i] + tuple((RANGE_LIST_LITERS_ARRAY[str(RANGE_LIST[i][2])]))

            return RANGE_LIST

    except Exception as _ex:
        print("[INFO] Error while working with PostrgeSQL ", _ex)

    finally:
        if connection:
            connection.close()


def take_liters(RANGE_LIST):
    ARRAY_RANGE_TIMESTAMP_MILLISEC = []
    temp = 0
    for i in RANGE_LIST:
        for y in range(3):
            if (y == 2):
                x = RANGE_LIST[temp][y]
                x = x*1000 #sec to millisec
                x = str(x)
                ARRAY_RANGE_TIMESTAMP_MILLISEC.append(x)
        temp += 1

    try:
        # открываем соединение с базой
        connection = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as cursor:
            # запрос на получение типов техники
            cursor.execute(
                f"""select distinct eqmt from history_fuel"""
            )
            TECH_ID = cursor.fetchall()

            # запросы на получения листа литров
            RANGE_LIST_LITERS_ARRAY = {}
            TEMP_ARRAY = []
            temp = 0

            for i in ARRAY_RANGE_TIMESTAMP_MILLISEC:
                for y in TECH_ID:
                    cursor.execute(
                        f"""SELECT eqmt, liters FROM history_fuel WHERE time_created >= {i} AND eqmt = {y[0]} ORDER BY time_created ASC LIMIT 1"""
                    )
                    x = cursor.fetchone()
                    TEMP_ARRAY.append(x)
                TECH_ID_QTY = [len(TECH_ID)]
                RANGE_LIST_LITERS_ARRAY[i[:-3]] = TECH_ID_QTY+TEMP_ARRAY #millisec to sec
                TEMP_ARRAY = []
                temp+=1

        return RANGE_LIST_LITERS_ARRAY

    except Exception as _ex:
        print("[INFO] Error while working with PostrgeSQL ", _ex)

    finally:
        if connection:
            connection.close()

def calc_fuel(RANGE_LIST):
    print("За выбранный диапазон смен установлено:")
    iter1 = 0 #итерация первого уровня
    total_change = []
    for i in range(RANGE_LIST[0][3]):
        total_change.append(0)

    for i in RANGE_LIST:
        if iter1!=len(RANGE_LIST)-1:
            print(f"Дата: {i[0]}, смена: {i[1]}")
            for y in range(i[3]):
                pos = 4+y
                symbol=""
                if(RANGE_LIST[iter1+1][pos][1]-i[pos][1]>0):
                    symbol = "+"
                else:
                    total_change[y]=total_change[y]+abs(RANGE_LIST[iter1+1][pos][1]-i[pos][1])

                print(f"Техника: {i[pos][0]}, начальный уровень топлива: {i[pos][1]}, конечный уровень топлива: {RANGE_LIST[iter1+1][pos][1]}, изменение уровня топлива: {symbol}{RANGE_LIST[iter1+1][pos][1]-i[pos][1]} ")
        iter1+=1
        if(iter1==len(RANGE_LIST)):
            for u in range(len(total_change)):
                print(f"Всего израсходовано топлива техникой {i[4+u][0]}: {total_change[u]}")


# За выбранный диапазон смен установлено:
# Дата: {}, смена: {},
# техника: {}, начальный уровень топлива: {}, конечный уровень топлива: {}, изменение уровня топлива: {}



#
# Вывести на графике? (да/нет):

def show_graphic(USER_RANGE):
    try:
        # открываем соединение с базой
        connection = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as cursor:
            ARRAY_RANGE_TIMESTAMP_MILLISEC = []
            for i in range(2):
                x = USER_RANGE[4+i]
                x = x * 1000  # sec to millisec
                x = str(x)
                ARRAY_RANGE_TIMESTAMP_MILLISEC.append(x)

            # запрос на получение списка изменения топлива
            cursor.execute(
                """SELECT eqmt, liters FROM history_fuel WHERE time_created >= %s AND time_created <= %s""",
                (ARRAY_RANGE_TIMESTAMP_MILLISEC[0], ARRAY_RANGE_TIMESTAMP_MILLISEC[1])
            )
            LIST_OF_FUEL = cursor.fetchall()


            show_plot(LIST_OF_FUEL)


    except Exception as _ex:
        print("[INFO] Error while working with PostrgeSQL ", _ex)

    finally:
        if connection:
            connection.close()




#
# вывести диапазон дат
# ввод даты начала
# вывести диапазон смен на дату
# ввод смены начала
# вывести диапазон дат
# ввод даты окончания
# вывести диапазон смен
# ввод смены окончания
#
# забрать timestamps начала и окончания диапазона
# найти ближайший вверх timestamp в истории начала
# найти ближайший вверх timestamp в истории окончания
# забрать диапазон в дикт
# разделить дикты по технике
# создать дикты изменения топлива
# вывести их на графике
#
# расчет расхода топлива общий:
# натуральные величины список
# тенденция список
# наибольшее натуральное
# наименьшее натуральное
# разница между max и min натуральных


# расчет расхода топлива по сменам:
# натуральные величины список
# тенденция список
# наибольшее натуральное
# наименьшее натуральное
# разница между max и min натуральных
# наибольший расход подряд разница ЗА СМЕНУ
#
# За выбранный диапазон смен установлено:
# Дата: {}, смена: {}, техника: {}, начальный уровень топлива: {}, конечный уровень топлива: {}, изменение уровня топлива: {}
# Дата: {}, смена: {}, начальный уровень топлива: {}, конечный уровень топлива: {}, изменение уровня топлива: {}
# Дата: {}, смена: {}, начальный уровень топлива: {}, конечный уровень топлива: {}, изменение уровня топлива: {}
# Дата: {}, смена: {}, начальный уровень топлива: {}, конечный уровень топлива: {}, изменение уровня топлива: {}
# Дата: {}, смена: {}, начальный уровень топлива: {}, конечный уровень топлива: {}, изменение уровня топлива: {}
# Дата: {}, смена: {}, начальный уровень топлива: {}, конечный уровень топлива: {}, изменение уровня топлива: {}
# Дата: {}, смена: {}, начальный уровень топлива: {}, конечный уровень топлива: {}, изменение уровня топлива: {}
# Дата: {}, смена: {}, начальный уровень топлива: {}, конечный уровень топлива: {}, изменение уровня топлива: {}
# Дата: {}, смена: {}, начальный уровень топлива: {}, конечный уровень топлива: {}, изменение уровня топлива: {}
# Дата: {}, смена: {}, начальный уровень топлива: {}, конечный уровень топлива: {}, изменение уровня топлива: {}
#
# Вывести на графике? (да/нет):
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
