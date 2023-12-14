from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analysit',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Fransico, USA',
        'salary': '$150,000'
    }
]

#-- api route --#
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


@app.route("/")
def landing_page():
    return render_template('index.html', jobs=JOBS, company_name="HZDR")


def main(app):
    app.run(host='0.0.0.0', debug=True)
    return 0

if __name__ == "__main__":
    main(app)
