from flask import Flask, render_template, request, redirect, url_for
import os
import requests

app = Flask(__name__)


@app.route('/ask')
def ask_for_age():
    return render_template('ask.template.html')


@app.route('/ask', methods=["POST"])
def show_if_can_vote():
    age = int(request.form.get('age'))
    if age >= 21:
        return "Can vote"
    else:
        return "Wait 5 years later"


@app.route('/bmi')
def show_bmi_form():
    return render_template('bmi.template.html')


@app.route('/bmi', methods=["POST"])
def calculate_bmi():
    weight = float(request.form.get('weight'))
    height = float(request.form.get('height'))
    bmi = weight / (height**2)
    return render_template('bmi_results.template.html', bmi=bmi)


@app.route('/currency')
def show_currency_form():
    return render_template('currency.template.html')


@app.route('/currency', methods=["POST"])
def process_currency_form():
    from_cur = request.form.get('from_cur')
    to_cur = request.form.get('to_cur')
    apikey = "K6V8A6XEX6OQVJCW"
    url = 'https://www.alphavantage.co/query'

    r = requests.get(url, {
        'function': "CURRENCY_EXCHANGE_RATE",
        'from_currency': from_cur,
        'to_currency': to_cur,
        'apikey': apikey
    })

    data = r.json()
    exchange_rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

    return render_template('currency_rates.template.html', from_cur=from_cur,
                           to_cur=to_cur, exchange_rate=exchange_rate)


@app.route('/user')
def show_user_form():
    return render_template('user.template.html')


@app.route('/user', methods=["POST"])
def process_user_form():
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    email = request.form.get('email')

    errors = []
    # check first name
    # use the len() function to check the length of strings
    if first_name is None or len(first_name) < 4:
        errors.append("Your first name must have more than 3 characters")

    if first_name is None or len(first_name) > 20:
        errors.append("Your first name cannot have more than 20 characters")

    if last_name is None or len(last_name) < 3:
        errors.append("Your last name must have 3 or more characters")

    if last_name is None or len(last_name) > 20:
        errors.append("Your last name cannot have more than 20 characters")

    if email is None or "@" not in email:
        errors.append("Your email address is invalid")

    if len(errors) == 0:
        return "Success!"
    else:
        return render_template('user.template.html', errors=errors)

@app.route('/userv2')
def show_advanced_user_form():
    return render_template('user.template.v2.html', errors={}, old_data={})


@app.route('/userv2', methods=["POST"])
def process_advanced_user_form():
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    email = request.form.get('email')

    errors = {}
    if first_name is None or len(first_name) < 4:
        errors["first_name"] = "Your first name must have more than 3 characters"

    if first_name is None or len(first_name) > 20:
        errors["first_name"] = "Your first name cannot have more than 20 characters"

    if last_name is None or len(last_name) < 3:
        errors["last_name"] = "Your last name must have 3 or more characters"

    if last_name is None or len(last_name) > 20:
        errors["last_name"] = "Your last name cannot have more than 20 characters"

    if email is None or "@" not in email:
        errors["email"] = "Your email address is invalid"

    if len(errors) == 0:
        return 'success'
    else:
        return render_template('user.template.v2.html', errors=errors, old_data=request.form)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
