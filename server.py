from flask import Flask, request, redirect, render_template, url_for, session, flash
from functools import wraps
import api_handler
import json


app = Flask(__name__)


def login_required(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("For this you need to log in")
            return redirect(url_for('login', next=request.url))
        return function(*args, **kwargs)
    return decorated_function


@app.route('/login')
def login():
    pass


@app.route('/')
def index():
    planets = api_handler.get_all("planets")
    len(planets.order_by("diameter"))
    return render_template('index.html', planets=planets)


@app.route('/<planet_name>', methods=['POST', 'GET'])
def get_residents(planet_name):
    residents = api_handler.get_residents_by_planet(planet_name)
    json_residents = json.dumps(residents)
    return redirect(url_for('index.html', json_residents=json_residents))


if __name__ == '__main__':
    app.secret_key = 'capra'
    app.run(
        host='0.0.0.0',
        port=5000,
        debug='True'
    )
