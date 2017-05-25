from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    pass


@app.route('mentors')
def mentors():
    pass


@app.route('all-school')
def all_school():
    pass


@app.route('/mentors-by-country')
def mentors_by_country():
    pass


@app.route('/contacts')
def contacts():
    pass


@app.route('/applicants')
def applicants():
    pass


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    pass


if __name__ == '__main__':
    app.run()
