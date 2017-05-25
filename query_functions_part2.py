from data_manager import access_db


@access_db
def mentors():
    query_command = "SELECT mentors.first_name, mentors.last_name, schools.name, schools.country \
                     FROM mentors LEFT OUTER JOIN schools \
                     USING (city) \
                     ORDER BY mentors.id;"
    return query_command


@access_db
def all_school():
    query_command = "SELECT mentors.first_name, mentors.last_name, schools.name, schools.country \
                     FROM mentors RIGHT OUTER JOIN schools \
                     USING (city) \
                     ORDER BY mentors.id;"
    return query_command


@access_db
def mentors_by_country():
    query_command = "SELECT schools.country AS country, COUNT(mentors.id) AS count \
                     FROM mentors RIGHT OUTER JOIN schools \
                     USING (city) \
                     GROUP BY schools.country \
                     ORDER BY schools.country;"
    return query_command


@access_db
def contacts():
    query_command = "SELECT schools.name, mentors.first_name, mentors.last_name \
                     FROM mentors JOIN schools ON schools.contact_person = mentors.id \
                     ORDER BY schools.name;"
    return query_command
