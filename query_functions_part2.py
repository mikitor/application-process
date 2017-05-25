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
