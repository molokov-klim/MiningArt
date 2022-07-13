import datetime

import psycopg2
from config import host, user, password, db_name, port


def check_fuel():

    try:
        #открываем соединение с базой
        connection = psycopg2.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=db_name
            )

        with connection.cursor() as cursor:
            #запрос на минимальную дату в сменах
            cursor.execute(
                    "SELECT min(shiftdate) FROM shifts"
                )

            MIN_DATE = cursor.fetchone()
            MIN_DATE = (MIN_DATE[0])

            #запрос на максимальную дату в сменах
            cursor.execute(
                "SELECT max(shiftdate) FROM shifts"
            )

            MAX_DATE = cursor.fetchone()
            MAX_DATE = MAX_DATE[0]

            #ввод пользователем даты начала интересующего его диапазона
            USER_DATE_START = input(f"Доступен временной дипазон с {MIN_DATE} по {MAX_DATE}. Пожалуйста введите дату начала нужного диапазона в формате ГГГГ-ММ-ДД: ")
            #FORMAT = "%Y-%m-%d"
            #USER_DATE_START = datetime.datetime.strptime(USER_DATE_START, FORMAT)


            #конвертация ввода в tuple, чтобы использовать в psycopg2
            USER_DATE_START = (USER_DATE_START,)
            #print(f"USER_DATE_START {type(USER_DATE_START)}{USER_DATE_START}")

            #запрос смен на дату
            cursor.execute(
                """SELECT shiftdate, shift, crew FROM shifts WHERE shiftdate = %s""", (USER_DATE_START[0],)
            )

            SHIFT_START = cursor.fetchall()

            #print(len(SHIFT_START))

            #вывод доступных смен на дату
            print("На выбранную дату доступны смены:")
            for elem_tuple in SHIFT_START:
                print(f"Дата: {elem_tuple[0]}, смена: {elem_tuple[1]}, команда: {elem_tuple[2]}")

            #ввод смены начала диапазона
            SHIFT_START_NUMBER = input("Пожалуйста введите номер смены: ")


            #print(f"На выбранную дату доступны смены: SHIFT_START[0][0]")

            #print(cursor.fetchall())

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

            print(f"Выбран диапазон: Начало - дата {USER_DATE_START[0]}, смена {SHIFT_START_NUMBER}; Окончание - дата {USER_DATE_END[0]}, смена {SHIFT_END_NUMBER}")

    except Exception as _ex:
        print("[INFO] Error while working with PostrgeSQL ", _ex)

    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")









#вывести диапазон дат
#ввод даты начала
#вывести диапазон смен на дату
#ввод смены начала
#вывести диапазон дат
#ввод даты окончания
#вывести диапазон смен
#ввод смены окончания
#
#забрать timestamps начала и окончания диапазона
#найти ближайший вверх timestamp в истории начала
#найти ближайший вверх timestamp в истории окончания
#забрать диапазон в дикт
#разделить дикты по технике
#создать дикты изменения топлива
#вывести их на графике
#
#расчет расхода топлива:
#натуральные величины список
#тенденция список
#наибольшее натуральное
#наименьшее натуральное
#разница между max и min натуральных
#наибольший расход подряд разница ЗА СМЕНУ