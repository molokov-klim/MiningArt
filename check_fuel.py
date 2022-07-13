import datetime

import psycopg2
from config import host, user, password, db_name, port


def show_max_range():
    #RANGE_START = range_start();
    try:
        connection = psycopg2.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=db_name
            )

        with connection.cursor() as cursor:
            cursor.execute(
                    "SELECT min(shiftdate) FROM shifts"
                )

            MIN_DATE = cursor.fetchone()
            MIN_DATE = (MIN_DATE[0])
            print(f"{MIN_DATE}")

            cursor.execute(
                "SELECT max(shiftdate) FROM shifts"
            )

            MAX_DATE = cursor.fetchone()
            MAX_DATE = MAX_DATE[0]
            print(f"{MAX_DATE}")
            USER_DATE_START = input(f"Доступен временной дипазон с {MIN_DATE} по {MAX_DATE}. Пожалуйста введите дату начала нужного диапазона в формате ГГГГ-ММ-ДД:")
            FORMAT = "%Y-%m-%d"
            USER_DATE_START = datetime.datetime.strptime(USER_DATE_START, FORMAT)
            USER_DATE_END = input(f"Пожалуйста введите дату окончания нужного диапазона в формате ГГГГ-ММ-ДД:")
            USER_DATE_END = datetime.datetime.strptime(USER_DATE_END, FORMAT)

            



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