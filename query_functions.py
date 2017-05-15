from data_manager import access_db


@access_db
def mentor_full_names():
    query_command = "SELECT first_name, last_name FROM mentors;"
    return query_command


@access_db
def mentor_nick_names_miskolc():
    query_command = "SELECT nick_name FROM mentors WHERE city='Miskolc';"
    return query_command


@access_db
def find_applicant_by_first_name():
    query_command = "SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number FROM applicants WHERE first_name='Carol';"
    return query_command


@access_db
def find_applicant_by_email():
    query_command = "SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number FROM applicants WHERE email LIKE'%@adipiscingenimmi.edu';"
    return query_command


@access_db
def add_new_applicant():
    query_command = "INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) VALUES ('Markus', 'Schaffarzyk', '0036020/725-2666', 'sjnovus@groovecoverage.com', '54823');"
    return query_command


@access_db
def find_applicant_by_applicantion_code():
    query_command = "SELECT * FROM applicants WHERE application_code='54823';"
    return query_command


@access_db
def update_applicant_phone_number():
    query_command = "UPDATE applicants SET phone_number='003670/223-7459' WHERE first_name='Jemima' AND last_name='Foreman';"
    return query_command


@access_db
def find_applicant_by_full_name_and_check_phone():
    query_command = "SELECT * FROM applicants WHERE first_name='Jemima' AND last_name='Foreman' AND phone_number IS NOT NULL;"
    return query_command


@access_db
def delete_applicant_by_email():
    query_command = "DELETE FROM applicants WHERE email LIKE '%mauriseu.net';"
    return query_command
