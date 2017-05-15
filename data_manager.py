import psycopg2


def access_db(some_function):
    def wrapper():
        try:
            # setup connection string
            connect_str = "dbname='miki' user='miki' host='localhost' password='123456789gl'"
            # use our connection values to establish a connection
            conn = psycopg2.connect(connect_str)
            # set autocommit option, to do every query when we call it
            conn.autocommit = True
            # create a psycopg2 cursor that can execute queries
            cursor = conn.cursor()

            query_command = some_function()
            cursor.execute(query_command)

            table = cursor.fetchall()
            return table
        except Exception as e:
            print("Uh oh, can't connect. Invalid dbname, user or password?")
            return e
    return wrapper
