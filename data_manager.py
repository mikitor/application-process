import psycopg2


def access_db(some_function):
    def wrapper():
        try:
            # export the credentials into an external config file
            connect_str = "dbname='miki' user='miki' host='localhost' password='123456789gl'"
            conn = psycopg2.connect(connect_str)
            conn.autocommit = True
            cursor = conn.cursor()

            query_command = some_function()
            cursor.execute(query_command)

            table = cursor.fetchall()
            return table
        except Exception as e:
            print("Uh oh, can't connect. Invalid dbname, user or password?")
            return e
    return wrapper
