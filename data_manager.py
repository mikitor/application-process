import psycopg2
import configuration


def access_db(some_function):
    def wrapper():
        try:
            # CONNECTION_DATA holds the credential information in a dictionary format
            connection_data = configuration.CONNECTION_DATA
            connect_string = "dbname='{dbname}' user='{user}' host='{host}' password='{password}'"
            connect_string = connect_string.format(**connection_data)
            conn = psycopg2.connect(connect_string)
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
