# Import statements necessary
from flask import Flask, render_template

from lab3_code import Bank
from lab3_code import Dollar, Yuan, Pound

import sys

# Set up application
app = Flask(__name__)

# Routes
@app.route('/')
def hello_app():
    return '<h1>Welcome to the banking application!!</h1>'

@app.route('/bank/<bank_name>')
def hello_bank(bank_name):
    bank = Bank(bank_name)
    return '<h1>Welcome to {}</h1>'.format(bank_name)

@app.route('/dollar/<int:amt>')
def demo_dollar(amt):
    dollar = Dollar(amt)
    return '<i>{}</i>'.format(dollar)

@app.route('/yuan/<int:amt>')
def demo_yuan(amt):
    yuan = Yuan(amt)
    return '<i>{}</i>'.format(yuan)

@app.route('/pound/<int:amt>')
def demo_pound(amt):
    pound = Pound(amt)
    return '<i>{}</i>'.format(pound)

@app.route('/bank/<name>/<currency>/<int:value>')
def new_word(name, currency: str, value):
    currency_ref_string = currency.lower().capitalize()
    currency_ref = getattr(sys.modules[__name__], currency_ref_string)
    bank = Bank(name, currency_ref, value)
    return '<b>Welcome to the {} bank! {}</b>'.format(
        bank.name,
        bank
    )

if __name__ == '__main__':
	app.run(debug=True)