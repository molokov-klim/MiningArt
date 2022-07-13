import psycopg2
from config import host, user, password, db_name

def check_fuel():
    #RANGE_START = range_start();
    try:
        connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )

        with connection.cursor() as cursor:
            cursor.execute(
                    "SELECT min(shiftdate) FROM shifts"
                )

            MIN_DATE = cursor.fetchone()
            print(f"{MIN_DATE}")

            cursor.execute(
                "SELECT max(shiftdate) FROM shifts"
            )

            MAX_DATE = cursor.fetchone()
            print(f"{MAX_DATE}")


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
#