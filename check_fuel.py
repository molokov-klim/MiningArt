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


