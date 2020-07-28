from flask import Flask, render_template, request, redirect, url_for
import json
import os


def save():
    with open("db.json", "w") as file_ptr:
        json.dump(database, file_ptr)


def load():
    with open("db.json", "r") as file_ptr:
        database = json.load(file_ptr)
    return database


app = Flask(__name__)

# global list to serve as database
database = load()


@app.route('/')
def show_all():
    return render_template("show_all.template.html", database=database)


@app.route('/add_report')
def show_add_report_form():
    return render_template('add_report_form.template.html')


@app.route('/add_report', methods=["POST"])
def process_add_report():
    location = request.form.get('location')
    comments = request.form.get('comments')
    crowd_density = request.form.get('density')
    activity = request.form.getlist('activity')

    new_report = {
        "id": len(database) + 1,
        "location": location,
        "comments": comments,
        "crowd_density": crowd_density,
        "activity": activity
    }

    database.append(new_report)
    save()

    # go back to the show all page
    return redirect(url_for('show_all'))


@app.route('/edit_report/<int:report_id>')
def show_update_form(report_id):

    # fetch the report by the id
    report = None
    for r in database:
        if r["id"] == report_id:
            report = r
            break

    return render_template('edit_report.template.html', report=report)


@app.route('/edit_report/<int:report_id>', methods=["POST"])
def update_report(report_id):
    # find the INDEX of the report in the database list
    wanted_report = None
    index_of_report = -1
    for index, report in enumerate(database):
        if report["id"] == report_id:
            wanted_report = report
            index_of_report = index

    # by this point,
    # index_of_report is the position of the report we want
    # wanted_report is the actual report that we want
    # modify the report inside the database
    wanted_report["location"] = request.form.get('location')
    wanted_report["comments"] = request.form.get('comments')
    wanted_report["crowd_density"] = request.form.get("density")
    wanted_report["activity"] = request.form.getlist("activity")

    # reassign the report back to the database at the correct index
    database[index_of_report] = wanted_report

    # save the file
    save()

    return redirect(url_for('show_all'))


@app.route('/delete_report/<int:report_id>')
def confirm_to_delete_report(report_id):
    report = None
    for r in database:
        if r["id"] == report_id:
            report = r
            break

    return render_template('ask_if_delete.template.html', report=report)


@app.route('/delete_report/<int:report_id>', methods=["POST"])
def delete_report(report_id):

    # find the index to delete for the report
    index_to_delete = -1
    for index, r in enumerate(database):
        if r["id"] == report_id:
            index_to_delete = index
            break

    # remove the element at `index_to_delete`
    del database[index_to_delete]

    save()

    return redirect(url_for('show_all'))


@app.route('/api/dummy', methods=["POST"])
def echo():
    data = request.json.get('data')
    return {
        "data": data
    }


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
