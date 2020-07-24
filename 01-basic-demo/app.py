# boilerplate
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route('/')
def home():
    fname = "Paul"
    lname = "Chor"
    return render_template("home.template.html",
                           first_name=fname, last_name=lname
                           )


@app.route('/about-our-fantastic-web-store')
def about_us():

    return render_template('about.template.html')


# paramterized routes
@app.route('/add/<n1>/<n2>')
def add_two(n1, n2):
    total = int(n1) + int(n2)
    return render_template('math.template.html', num1=n1,
                           num2=n2, result=total)


@app.route('/products')
def show_products():
    # returning a dictionary will send back a JSON object to the client
    return {
        "id": 1,
        "product-name": "Anvil",
        "desc": "For dropping on roadrunner's head"
    }


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
