import psycopg2
from data_manager import access_db


@access_db
def full_name_mentors():
    query_command = "SELECT first_name, last_name FROM mentors;"
    return query_command


@access_db
def nick_names_miskolc():
    query_command = "SELECT nick_name FROM mentors WHERE city='Miskolc';"
    return query_command

if __name__ == '__main__':
    print(nick_names_miskolc())
