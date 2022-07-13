import psycopg2
from config import host, user, password, db_name, port


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

            # ввод пользователем даты начала интересующего его диапазона
            USER_DATE_START = input(
                f"Доступен временной дипазон с {MIN_DATE} по {MAX_DATE}. Пожалуйста введите дату начала нужного диапазона в формате ГГГГ-ММ-ДД: ")

            # конвертация ввода в tuple, чтобы использовать в psycopg2
            USER_DATE_START = (USER_DATE_START,)

            # запрос смен на дату
            cursor.execute(
                """SELECT shiftdate, shift, crew FROM shifts WHERE shiftdate = %s""", (USER_DATE_START[0],)
            )
            SHIFT_START = cursor.fetchall()

            # вывод доступных смен на дату
            print("На выбранную дату доступны смены:")
            for elem_tuple in SHIFT_START:
                print(f"Дата: {elem_tuple[0]}, смена: {elem_tuple[1]}, команда: {elem_tuple[2]}")

            # ввод смены начала диапазона
            SHIFT_START_NUMBER = input("Пожалуйста введите номер смены: ")

            # ввод пользователем даты окончания интересующего его диапазовна
            USER_DATE_END = input(f"Пожалуйста введите дату окончания нужного диапазона в формате ГГГГ-ММ-ДД: ")
            # конвертация ввода в tuple, чтобы использовать в psycopg2
            USER_DATE_END = (USER_DATE_END,)

            # запрос смен на дату
            cursor.execute(
                """SELECT shiftdate, shift, crew FROM shifts WHERE shiftdate = %s""", (USER_DATE_END[0],)
            )
            SHIFT_END = cursor.fetchall()

            # вывод доступных смен на дату
            print("На выбранную дату доступны смены:")
            for elem_tuple in SHIFT_END:
                print(f"Дата: {elem_tuple[0]}, смена: {elem_tuple[1]}, команда: {elem_tuple[2]}")

            # ввод смены окончания диапазона
            SHIFT_END_NUMBER = input("Пожалуйста введите номер смены: ")

            print(
                f"Выбран диапазон: Начало - дата {USER_DATE_START[0]}, смена {SHIFT_START_NUMBER}; Окончание - дата {USER_DATE_END[0]}, смена {SHIFT_END_NUMBER}")

            USER_RANGE = (USER_DATE_START[0], SHIFT_START_NUMBER, USER_DATE_END[0], SHIFT_END_NUMBER)
            return USER_RANGE

    except Exception as _ex:
        print("[INFO] Error while working with PostrgeSQL ", _ex)

    finally:
        if connection:
            connection.close()


# функция поиска соответствия timestamp
def take_timestamps(USER_RANGE):
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
                """SELECT shiftstart_epoch FROM shifts WHERE shiftdate = %s and shift = %s""", (USER_RANGE[0], USER_RANGE[1])
            )

            SHIFT_TIMESTAMP_START = cursor.fetchone()

            # запрос на timestamp окончания диапазона
            cursor.execute(
                """SELECT shiftstart_epoch FROM shifts WHERE shiftdate = %s and shift = %s""", (USER_RANGE[2], USER_RANGE[3])
            )

            SHIFT_TIMESTAMP_END = cursor.fetchone()

            #конвертация в str, конкатенация разрядности и объединение в tuple
            temp = SHIFT_TIMESTAMP_START[0]
            temp = str(temp) + "000"
            SHIFT_TIMESTAMP_START = temp
            temp = SHIFT_TIMESTAMP_END[0]
            temp = str(temp) + "000"
            SHIFT_TIMESTAMP_END = temp
            SHIFT_TIMESTAMPS = (SHIFT_TIMESTAMP_START, SHIFT_TIMESTAMP_END)

            # запрос на timestamp начала диапазона в истории топлива
            cursor.execute(
                """SELECT time_created FROM history_fuel WHERE time_created >= %s ORDER BY time_created ASC LIMIT 1""", (SHIFT_TIMESTAMPS[0],)
            )

            FUEL_TIMESTAMP_START = cursor.fetchone()

            # запрос на timestamp окончания диапазона в истории топлива
            cursor.execute(
                """SELECT time_created FROM history_fuel WHERE time_created >= %s ORDER BY time_created ASC LIMIT 1""",
                (SHIFT_TIMESTAMPS[1],)
            )

            FUEL_TIMESTAMP_END = cursor.fetchone()

            FUEL_TIMESTAMPS = (FUEL_TIMESTAMP_START[0], FUEL_TIMESTAMP_END[0])

            return FUEL_TIMESTAMPS

    except Exception as _ex:
        print("[INFO] Error while working with PostrgeSQL ", _ex)

    finally:
        if connection:
            connection.close()


# функция указания единицы техники
def take_tech_id(FUEL_TIMESTAMPS):
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
            # запрос на доступные единицы техники
            cursor.execute(
                """SELECT DISTINCT eqmt FROM history_fuel WHERE time_created > %s and time_created < %s""", (FUEL_TIMESTAMPS[0],FUEL_TIMESTAMPS[1])
            )

            TECH_TUPLE = cursor.fetchall()
            print("На выбранный диапазон доступны единицы техники: ")
            for i in TECH_TUPLE:
                print(f"{i[0]}")
            TECH_ID = input("Пожалуйста введите номер единицы техники: ")

            return TECH_ID

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
# расчет расхода топлива:
# натуральные величины список
# тенденция список
# наибольшее натуральное
# наименьшее натуральное
# разница между max и min натуральных
# наибольший расход подряд разница ЗА СМЕНУ
