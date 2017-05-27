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
    table_header = ['']
    return render_template('table.html', table=table)


@app.route('/all-school')
def all_school():
    table = query_functions_part2.all_school()
    return render_template('table.html', table=table)


@app.route('/mentors-by-country')
def mentors_by_country():
    table = query_functions_part2.mentors_by_country()
    return render_template('table.html', table=table)


@app.route('/contacts')
def contacts():
    table = query_functions_part2.contacts()
    return render_template('table.html', table=table)


@app.route('/applicants')
def applicants():
    table = query_functions_part2.applicants()
    return render_template('table.html', table=table)


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    table = query_functions_part2.applicants_and_mentors()
    return render_template('table.html', table=table)


if __name__ == '__main__':
    app.run(debug=True)
