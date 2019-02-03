# Project-01-repo-si507

This project demostrate a simple Flask app and simulates a bank lookup system.

## Prerequisites

1. Clone this repo to your local.

1. Cd to the project directory. Please install the dependencies before you start. Create a virtual envionment, then simply run `pip install -r requirements.txt`.

## Run the app

1. Start the server by running `python SI507_project1.py runserver`.

1. Navigate to `http://localhost:5000/` and enjoy!

1. Routes available and what they do are as below:

    1. `http://localhost:5000/<bank_name>` greets you a short message from the bank, given the bank name specified by you.
    1. `http://localhost:5000/dollar/<amount>`, `http://localhost:5000/yuan/<amount>` and `http://localhost:5000/pound/<amount>` give you a formal representation of the currency with the amount you specified.
    1. `http://localhost:5000/bank/<bank_name>/<currency>/<value>` gives you a brief summary of the bank, given the name of the bank, the currency its using, and an amount of that currency, specified by you.


## Structure

All of the data model (i.e. classes) are defined in `lab3_code.py`, and the main Flask entry point is defined in `SI507_project1.py`.

Since the routes are relatively simple, `SI507_project1.py` also contains all the routes instead of a saparate file.