from flask import Flask, render_template
import psycopg2
import query_functions_part2


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('layout.html')


@app.route('/mentors')
def mentors():
    table = query_functions_part2.mentors()
    table_header = ['Mentor name', 'School', 'Country']
    return render_template('table.html', table=table, table_header=table_header)


@app.route('/all-school')
def all_school():
    table = query_functions_part2.all_school()
    table_header = ['Mentor name', 'School', 'Country']
    return render_template('table.html', table=table, table_header=table_header)


@app.route('/mentors-by-country')
def mentors_by_country():
    table = query_functions_part2.mentors_by_country()
    table_header = ['Country', 'Number of mentors']
    return render_template('table.html', table=table, table_header=table_header)


@app.route('/contacts')
def contacts():
    table = query_functions_part2.contacts()
    table_header = ['School', 'Mentor name']
    return render_template('table.html', table=table, table_header=table_header)


@app.route('/applicants')
def applicants():
    table = query_functions_part2.applicants()
    table_header = ['Applicant first name', 'Application code', 'Application date']
    return render_template('table.html', table=table, table_header=table_header)


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    table = query_functions_part2.applicants_and_mentors()
    table_header = ['Applicant first name', 'Application code', 'Mentor first name', 'Mentor last name']
    return render_template('table.html', table=table, table_header=table_header)


if __name__ == '__main__':
    app.run(debug=True)
