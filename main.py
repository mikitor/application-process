import os
import psycopg2
import sys

import display
import query_functions
from data_manager import access_db


def choose():
    inputs = display.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        os.system('clear')
        table = query_functions.mentor_full_names()
        title_list = ['First name', 'Last name']
        display.print_table(table, title_list)
    elif option == "2":
        os.system('clear')
        table = query_functions.mentor_nick_names_miskolc()
        title_list = ['Nick name']
        display.print_table(table, title_list)
    elif option == "3":
        os.system('clear')
        table = query_functions.find_applicant_by_first_name()
        title_list = ['Full name', 'Phone number']
        display.print_table(table, title_list)
    elif option == "4":
        os.system('clear')
        table = query_functions.find_applicant_by_email()
        title_list = ['Full name', 'Phone number']
        display.print_table(table, title_list)
    elif option == "5":
        os.system('clear')
        query_functions.add_new_applicant()
        table = query_functions.find_applicant_by_applicantion_code()
        title_list = ['ID', 'First name', 'Last name', 'Phone number', 'Email', 'Application code']
        display.print_table(table, title_list)
    elif option == "6":
        os.system('clear')
        query_functions.update_applicant_phone_number()
        table = query_functions.find_applicant_by_full_name_and_check_phone()
        title_list = ['ID', 'First name', 'Last name', 'Phone number', 'Email', 'Application code']
        display.print_table(table, title_list)
    elif option == "7":
        os.system('clear')
        table = query_functions.delete_applicant_by_email()
        print('There is no such entry anymore!')
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Full names of Codecool mentors",
               "Nick names of mentors from Miskolc",
               "Find Carol",
               "Find an applicant by email",
               "Add new applicant",
               "Update applicant phone number",
               "Delete applicants with domain name"]

    display.print_menu("Main menu", options, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            display.print_error_message(err)


if __name__ == '__main__':
    main()
